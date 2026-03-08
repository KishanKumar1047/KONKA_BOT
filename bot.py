import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from groq import Groq

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

chat_memory = {}

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.chat_id
    user_message = update.message.text

    if user_id not in chat_memory:
        chat_memory[user_id] = []

    chat_memory[user_id].append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=chat_memory[user_id]
    )

    bot_reply = response.choices[0].message.content

    chat_memory[user_id].append({"role": "assistant", "content": bot_reply})

    await update.message.reply_text(bot_reply)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()