from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ====== BOT TOKEN ======
import os
TOKEN = os.getenv("TOKEN")




# ====== KANAL MA'LUMOTLARI ======
CHANNEL_USERNAME = "@saminov_app"   # kanal username
PROGRAM_MESSAGE_ID = 3              # kanal post ID

# ====== TUGMALAR ======
keyboard = ReplyKeyboardMarkup(
    [
        ["📥 Dasturni yuklash"],
        ["ℹ️ Info"]
    ],
    resize_keyboard=True
)

# ====== /start ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum!\n\nKerakli tugmani tanlang:",
        reply_markup=keyboard
    )

# ====== TUGMALAR HANDLER ======
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📥 Dasturni yuklash":
        await context.bot.forward_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL_USERNAME,
            message_id=PROGRAM_MESSAGE_ID
        )

    elif text == "ℹ️ Info":
        await update.message.reply_text(
            "Bu bot orqali dasturlarni tez va qulay yuklab olishingiz mumkin."
        )

    else:
        await update.message.reply_text(
            "Iltimos, pastdagi tugmalardan foydalaning."
        )

# ====== BOTNI ISHGA TUSHIRISH ======
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
