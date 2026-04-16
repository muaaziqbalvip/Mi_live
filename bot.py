import os
import time
import random
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT2_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

chat_history = {}

async def reply_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message
    if not message or not message.text:
        return

    chat_id = message.chat_id
    user_text = message.text

    time.sleep(random.randint(3, 4))

    if chat_id not in chat_history:
        chat_history[chat_id] = []

    chat_history[chat_id].append({"role": "user", "content": user_text})
    chat_history[chat_id] = chat_history[chat_id][-10:]

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are MI AI Bot 2. You are logical, slightly opposite opinion from Bot1 and continue conversation."},
            *chat_history[chat_id]
        ]
    }

    try:
        res = requests.post(GROQ_URL, headers=headers, timeout=20)
        reply = res.json()["choices"][0]["message"]["content"]
    except:
        reply = "⚠️ Bot2 error"

    chat_history[chat_id].append({"role": "assistant", "content": reply})

    await message.reply_text(f"🤖 Bot2: {reply}")


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_ai))
    print("Bot2 running...")
    app.run_polling()


if __name__ == "__main__":
    main()
