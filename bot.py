import time
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8455266168:AAG5MpcL307-KRnCITrXgHGrH04IO6cuizs"
CHAT_ID = 6754145366

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive and responding!")

async def notify_startup(app):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="🚀 Sidejob bot has started and is running.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.post_init = notify_startup

    print("Bot is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
