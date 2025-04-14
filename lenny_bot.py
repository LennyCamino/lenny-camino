import os
import telegram
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("🕊️ ¡Hola! Soy Lenny, tu guía en el Camino de Santiago.")

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot Lenny escuchando... Ctrl+C para detener")
app.run_polling()
