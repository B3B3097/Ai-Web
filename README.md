# VLESS Config Generator Bot

Telegram bot for creating and distributing VLESS configs via GitHub Pages.

## Structure

- `bot/` - Telegram bot code
- `core/` - VLESS config generation logic
  - `vless_generator.py` - Generate and parse VLESS configs
  - `github_manager.py` - GitHub API integration for config storage
- `configs/` - Generated configurations directory

## Features

- ✅ Only responds to @Weleredz
- ✅ Two buttons: "Get Proxy" and "Update"
- ✅ Generates VLESS WebSocket configs with TLS
- ✅ Stores configs in GitHub repository
- ✅ Supports GitHub Pages for hosting configs
- ✅ Automatic config updates with UUID preservation

## Setup

### 1. Create 3 Repositories

You'll need:
1. **Main bot repository** - This code
2. **Config storage repository** - For storing VLESS configs
3. **GitHub Pages repository** - For hosting configs (can be same as #2)

### 2. Get Telegram Bot Token

1. Message @BotFather on Telegram
2. Send `/newbot`
3. Follow instructions to get your token

### 3. Create GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope
3. Copy the token

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your values:
- `BOT_TOKEN` - Telegram bot token
- `GITHUB_TOKEN` - GitHub API token
- `CONFIG_REPO` - Config storage repo (format: owner/repo)
- `PAGES_REPO` - GitHub Pages repo (format: owner/repo)
- `VLESS_ADDRESS` - Your VLESS server domain
- `VLESS_PORT` - Server port (usually 443)
- `VLESS_PATH` - WebSocket path
- `VLESS_SNI` - Server Name Indication

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Bot

```bash
python bot/main.py
```

## Usage

1. Start the bot with `/start`
2. Click **"🔑 Get Proxy"** to generate a new VLESS config
3. Click **"🔄 Update"** to refresh your existing config

The bot will:
- Generate a unique VLESS config
- Store it in the GitHub repository
- Send you the config URL to use in your client

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Telegram   │────▶│  VLESS Bot   │────▶│   GitHub    │
│   User      │◀────│  (main.py)   │◀────│   API       │
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                    ┌──────┴──────┐
                    │             │
              ┌─────▼─────┐ ┌────▼─────┐
              │   VLESS   │ │  GitHub  │
              │ Generator │ │ Manager  │
              └───────────┘ └──────────┘
```

## License

Private repository
