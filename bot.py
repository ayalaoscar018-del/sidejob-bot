# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Get your bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN", "8455266168:AAG5MpcL307-KRnCITrXgHGrH04IO6cuizs")  # fallback to your token

# Example command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is running.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a help message.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
