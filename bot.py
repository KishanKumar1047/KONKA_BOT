import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)

from groq import Groq
from memory import get_user_memory, reset_memory
from rate_limiter import is_allowed

TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

client = Groq(api_key=GROQ_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I'm your AI assistant.\n\n"
        "Send me a message and I'll reply.\n\n"
        "Commands:\n"
        "/help - show help\n"
        "/reset - reset conversation"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Telegram Bot\n\n"
        "/start - start bot\n"
        "/help - show commands\n"
        "/reset - clear conversation memory"
    )


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    reset_memory(user_id)

    await update.message.reply_text("🧠 Memory cleared!")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    message = update.message.text

    if not is_allowed(user_id):
        await update.message.reply_text("⏳ Please wait before sending another message.")
        return

    memory = get_user_memory(user_id)

    memory.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=memory
    )

    reply = response.choices[0].message.content

    memory.append({
        "role": "assistant",
        "content": reply
    })

    await update.message.reply_text(reply)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("reset", reset))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

app.run_polling(drop_pending_updates=True)