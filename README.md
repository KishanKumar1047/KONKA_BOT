# 🤖 Telegram AI Bot

An AI-powered Telegram chatbot built using **Python**, **Groq API**, and **python-telegram-bot**.
The bot supports intelligent conversations, per-user memory, command handling, and rate limiting.

---

## 🚀 Features

* 🧠 **Conversation Memory**

  * The bot remembers conversation history for each user.

* 💬 **AI Chat**

  * Uses Groq LLM to generate intelligent responses.

* ⚙️ **Command Support**

  * `/start` – start the bot
  * `/help` – show help message
  * `/reset` – reset conversation memory

* ⏱ **Rate Limiting**

  * Prevents users from sending too many requests and exhausting API quota.

* ☁️ **Cloud Deployment**

  * Runs 24/7 using Railway.

---

## 📱 Telegram Bot

Scan the QR code below to open the bot in Telegram.

![Telegram Bot QR](![alt text](image.png))

Bot Username:

```
@KONA_H_BOT
```

---

## 🛠 Tech Stack

* Python
* python-telegram-bot
* Groq API
* Railway Deployment

---

## 📂 Project Structure

```
telegram-ai-bot
│
├── bot.py            # Main bot logic
├── memory.py         # Conversation memory system
├── rate_limiter.py   # Prevents API spam
│
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

Create environment variables before running:

```
TELEGRAM_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the bot:

```
python bot.py
```

---

## ☁️ Deployment

This project is deployed using **Railway**.

Steps:

1. Push code to GitHub
2. Connect repository to Railway
3. Add environment variables
4. Deploy

---

## 👨‍💻 Author

GitHub:
https://github.com/kishankumar1047

---

## 📌 Future Improvements

* 📄 PDF RAG chatbot
* 🎤 Voice message support
* 📊 Usage analytics
* 🧠 Advanced long-term memory
