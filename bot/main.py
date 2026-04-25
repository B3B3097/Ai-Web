"""
Telegram bot for VLESS config generation
"""
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from core import VLESSConfigGenerator, GitHubManager

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Allowed username
ALLOWED_USERNAME = "Weleredz"


class VLESSBot:
    """Telegram bot for VLESS config management"""
    
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.config_repo = os.getenv("CONFIG_REPO")  # Format: owner/repo
        self.pages_repo = os.getenv("PAGES_REPO")    # Format: owner/repo
        
        # Server configuration
        self.server_address = os.getenv("VLESS_ADDRESS", "your-domain.com")
        self.server_port = int(os.getenv("VLESS_PORT", "443"))
        self.server_path = os.getenv("VLESS_PATH", "/vless")
        self.server_sni = os.getenv("VLESS_SNI", "your-domain.com")
        
        # Initialize components
        self.generator = VLESSConfigGenerator()
        self.github = GitHubManager(
            token=self.github_token,
            repo_name=self.config_repo,
            pages_repo_name=self.pages_repo,
        )
        
        # User configs storage (in-memory, can be extended to database)
        self.user_configs = {}
        
    def is_allowed_user(self, username: str) -> bool:
        """Check if user is allowed to use the bot"""
        return username == ALLOWED_USERNAME
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        username = user.username
        
        if not self.is_allowed_user(username):
            await update.message.reply_text(
                "❌ Sorry, this bot is only available for @Weleredz"
            )
            return
        
        # Create keyboard with buttons
        keyboard = [
            [InlineKeyboardButton("🔑 Get Proxy", callback_data="get_proxy")],
            [InlineKeyboardButton("🔄 Update", callback_data="update_proxy")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"Welcome @{username}!\n\n"
            "Choose an option:",
            reply_markup=reply_markup,
        )
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button clicks"""
        query = update.callback_query
        user = query.from_user
        username = user.username
        
        if not self.is_allowed_user(username):
            await query.answer("❌ Access denied", show_alert=True)
            return
        
        await query.answer()
        
        if query.data == "get_proxy":
            await self.handle_get_proxy(query, username)
        elif query.data == "update_proxy":
            await self.handle_update_proxy(query, username)
    
    async def handle_get_proxy(self, query, username: str):
        """Generate and send a new VLESS config"""
        try:
            # Generate new config
            config = self.generator.generate_config(
                address=self.server_address,
                port=self.server_port,
                path=self.server_path,
                sni=self.server_sni,
                username=username,
            )
            
            # Upload to GitHub
            filename = self.github.upload_config(username, config)
            
            # Store config info
            self.user_configs[username] = {
                "config": config,
                "filename": filename,
            }
            
            # Send config to user
            await query.edit_message_text(
                f"✅ New VLESS config generated!\n\n"
                f"```\n{config}\n```\n\n"
                f"Config saved to: `{filename}`\n"
                f"You can update it anytime using the Update button.",
                parse_mode="Markdown",
            )
            
        except Exception as e:
            logger.error(f"Error generating config: {e}")
            await query.edit_message_text(
                "❌ Error generating config. Please try again later."
            )
    
    async def handle_update_proxy(self, query, username: str):
        """Update existing VLESS config"""
        try:
            # Check if user has existing config
            if username not in self.user_configs:
                # Try to get from GitHub
                existing_config = self.github.get_config(username)
                if existing_config:
                    self.user_configs[username] = {"config": existing_config}
                else:
                    await query.edit_message_text(
                        "⚠️ No existing config found.\n"
                        "Please use 'Get Proxy' first."
                    )
                    return
            
            # Generate new config with same UUID or new one
            old_config = self.user_configs[username].get("config", "")
            uuid_value = None
            
            # Try to extract UUID from old config
            try:
                parsed = self.generator.parse_config(old_config)
                uuid_value = parsed["uuid"]
            except:
                pass
            
            # Generate updated config
            config = self.generator.generate_config(
                address=self.server_address,
                port=self.server_port,
                path=self.server_path,
                sni=self.server_sni,
                username=username,
                uuid_value=uuid_value,
            )
            
            # Update on GitHub
            old_filename = self.user_configs[username].get("filename")
            filename = self.github.upload_config(username, config, old_filename)
            
            # Update stored config
            self.user_configs[username] = {
                "config": config,
                "filename": filename,
            }
            
            await query.edit_message_text(
                f"✅ Config updated successfully!\n\n"
                f"```\n{config}\n```\n\n"
                f"File: `{filename}`",
                parse_mode="Markdown",
            )
            
        except Exception as e:
            logger.error(f"Error updating config: {e}")
            await query.edit_message_text(
                "❌ Error updating config. Please try again later."
            )
    
    async def unknown_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle unknown commands"""
        user = update.effective_user
        username = user.username
        
        if not self.is_allowed_user(username):
            return
        
        await update.message.reply_text("Sorry, I don't understand that command.")
    
    def run(self):
        """Start the bot"""
        # Create application
        application = Application.builder().token(self.token).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CallbackQueryHandler(self.button_callback))
        application.add_handler(
            MessageHandler(filters.COMMAND, self.unknown_command)
        )
        
        # Start polling
        logger.info("Bot started...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """Main entry point"""
    # Validate environment variables
    required_vars = ["BOT_TOKEN", "GITHUB_TOKEN", "CONFIG_REPO"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {missing_vars}")
        logger.error("Please set BOT_TOKEN, GITHUB_TOKEN, and CONFIG_REPO")
        return
    
    # Create and run bot
    bot = VLESSBot()
    bot.run()


if __name__ == "__main__":
    main()
