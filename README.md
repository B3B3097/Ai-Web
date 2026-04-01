# Telegram AI Bot Mini App

## Project Overview
This project is a mini app that integrates with Telegram to provide AI-driven functionalities. The bot can respond to user queries, manage conversations, and perform tasks on behalf of users, leveraging multiple AI models.

## Features
- **Rate Limiting**: To manage server load and prevent abuse, the bot implements rate limiting, ensuring fair use across all users.
- **Multiple AI Models**: The bot supports various AI models, allowing users to choose the most suitable one for their tasks, enhancing versatility and performance.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/B3B3097/Ai-Web.git
   cd Ai-Web
   ```
2. Install the required dependencies:
   ```bash
   npm install
   ```
3. Set up your environment variables by creating a `.env` file in the root directory. The necessary environment variables are:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram Bot token getting from BotFather.
   - `AI_MODEL`: Specify the AI model you want to use.

## Usage Guide
- Start the bot:
   ```bash
   node index.js
   ```
- Interact with the bot on Telegram by sending commands and messages.

## Deployment Notes
- Ensure your server meets the requirements to run Node.js applications.
- Consider using a process manager like `pm2` to keep the bot running continuously.
- Monitor the logs for errors and performance metrics.

For more information, refer to the documentation and source code provided in this repository.