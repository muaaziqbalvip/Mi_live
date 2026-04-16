import os
import time
import random
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKE")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

async def reply_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # 3-4 sec delay (human-like thinking)
    time.sleep(random.randint(3, 4))

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are MI AI. You are smart, helpful, and reply in any language. Keep responses short and natural."},
            {"role": "user", "content": user_text}
        ]
    }

    try:
        res = requests.post(GROQ_URL, headers=headers, json=payload)
        data = res.json()
        reply = data["choices"][0]["message"]["content"]
    except:
        reply = "Sorry, abhi AI respond nahi kar raha 😕"

    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Auto reply EVERY message (no commands needed)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_ai))

    print("MI AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
