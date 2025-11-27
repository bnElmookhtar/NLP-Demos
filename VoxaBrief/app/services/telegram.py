from telethon import TelegramClient
import asyncio
import os 
from dotenv import load_dotenv

# Load environment variables from .env
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def send_telegram_message(chat_id: str, message: str):
    """
    Sends a message to a specified Telegram chat using a bot.

    Args:
        chat_id (str): The Telegram chat ID to send the message to.
        message (str): The message content to send.
    """
    async def main():
        # Create the Telegram client
        client = TelegramClient('bot_session', telegram_id, telegram_hash).start(bot_token=telegram_bot_token)
        
        # Send the message
        await client.send_message(chat_id, message)
        
        # Disconnect the client
        await client.disconnect()

    # Run the async function
    asyncio.run(main())