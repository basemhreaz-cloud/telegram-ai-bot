from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from google import genai
import os

BOT_TOKEN = os.getenv("8729159145:AAGk_0fgPlVyfUtu80jwY0J4Q45SUEnLtWc")
GEMINI_API_KEY = os.getenv("AQ.Ab8RN6IO7jXeoQl3CvdmBVe5PRtHLevOvNKMz0EEfMr3D6E1hg")

client = genai.Client(api_key=AQ.Ab8RN6IO7jXeoQl3CvdmBVe5PRtHLevOvNKMz0EEfMr3D6E1hg)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_text
    )

    await update.message.reply_text(response.text)

app = Application.builder().token(8729159145:AAGk_0fgPlVyfUtu80jwY0J4Q45SUEnLtWc).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot Started...")

app.run_polling()
