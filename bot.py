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

# memory (simple conversation context)
chat_history = {}

async def reply_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message
    if not message or not message.text:
        return

    chat_id = message.chat_id
    user_text = message.text

    # 🔥 group + private both show input (for conversation feel)
    print(f"USER [{chat_id}]: {user_text}")

    # 3–4 sec delay (human feel)
    time.sleep(random.randint(3, 4))

    # 🔥 keep last messages (conversation memory)
    if chat_id not in chat_history:
        chat_history[chat_id] = []

    chat_history[chat_id].append({"role": "user", "content": user_text})

    # limit memory
    chat_history[chat_id] = chat_history[chat_id][-10:]

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are MI AI in a Telegram group. "
                    "You are part of conversation. Reply naturally like chatting. "
                    "Keep responses short, engaging, and human-like."
                )
            },
            *chat_history[chat_id]
        ]
    }

    try:
        res = requests.post(GROQ_URL, headers=headers, json=payload, timeout=20)
        data = res.json()
        reply = data["choices"][0]["message"]["content"]

    except Exception as e:
        print("ERROR:", e)
        reply = "⚠️ AI temporarily down"

    # save AI reply in memory
    chat_history[chat_id].append({"role": "assistant", "content": reply})

    # 🔥 GROUP OUTPUT SHOW
    await message.reply_text(reply)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # 🔥 works in GROUP + PRIVATE both
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_ai))

    print("🤖 MI AI Conversation Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()
