import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from groq import Groq

TOKEN = os.environ.get("TELEGRAM_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content

    await update.message.reply_text(bot_reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling(drop_pending_updates=True)