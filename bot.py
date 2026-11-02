import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters

# Logging sozlamalari
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Telegram token
TELEGRAM_TOKEN = "8969489167:AAGF1DSBh4fMjPoD-BOUjtuBGAq0kTu14u0"

# /start buyrug'i bosilganda chiqadigan asosiy menyu (Tugmalar)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Stipendiya, Turar joy, Kontrakt, Bandlik", callback_data="block_1")],
        [InlineKeyboardButton("🌍 Xalqaro yo'nalishlar va Grantlar", callback_data="block_2")],
        [InlineKeyboardButton("📚 Dars jadvali, HEMIS va Ma'lumotnomalar", callback_data="block_3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        "Assalomu alaykum! Kerakli yo'nalishni tanlang va mas'ul menejerlar "
        "kontaktlarini oling:"
    )
    
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(welcome_text, reply_markup=reply_markup)

# Tugmalar bosilganda ishlaydigan qism
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Ortga qaytish uchun tugma
    back_keyboard = [[InlineKeyboardButton("🔙 Orqaga qaytish", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(back_keyboard)

    if query.data == "block_1":
        text = (
            "📌 **Xizmat yo'nalishlari:**\n"
            "• Stipendiya masalalari\n"
            "• Talabalar turar joyi xizmatlari\n"
            "• Shartnoma summalarini hisoblash\n"
            "• Bitiruvchilar bandligi va taqsimoti\n\n"
            "👤 **Mas'ul xodim:** Quryazov Dilshod\n"
            "• Telegram: [@Dilshod_Quryazov](https://t.me/Dilshod_Quryazov)\n"
            "• Tel: +998 97 790 60 69\n\n"
            "🔄 **Qo'shimcha murojaat uchun:**\n"
            "👤 Ro‘zmetov Toxir\n"
            "• Telegram: [@t_ruzmetov](https://t.me/t_ruzmetov)\n"
            "• Tel: +998 93 753 75 30"
        )
    elif query.data == "block_2":
        text = (
            "🌍 **Xalqaro yo'nalishlar va grantlar bo'yicha:**\n"
            "• Ingliz tilida ma’lumotnoma berish / Study certificates in English\n"
            "• Grant va mobillik dasturlari / Grants and mobility programs\n"
            "• Xorijda ta’lim olish va ro'yxatdan o'tish / Studying abroad & Registration\n\n"
            "👤 **Mas'ul xodim:** Ro‘zmetov Toxir\n"
            "• Telegram: [@t_ruzmetov](https://t.me/t_ruzmetov)\n"
            "• Tel: +998 93 753 75 30"
        )
    elif query.data == "block_3":
        text = (
            "📚 **O'quv jarayoni va HEMIS bo'yicha mas'ullar:**\n"
            "• Dars jadvali va imtihonlar, nazoratlar\n"
            "• Transkript va ma'lumotnomalar, talabalik guvohnomasi\n"
            "• HEMIS parolini tiklash, o'qishga qabul va ko'chirish\n\n"
            "👤 **Matchanova Fotima**\n"
            "• Telegram: [@Fotima_Matchanova](https://t.me/Fotima_Matchanova)\n"
            "• Tel: +998 93 562 99 08\n\n"
            "👤 **Xayitboyev Umrbek**\n"
            "• Tel: +998 87 526 11 91\n\n"
            "🔄 **Qo'shimcha murojaat uchun:**\n"
            "👤 Ro‘zmetov Toxir\n"
            "• Telegram: [@t_ruzmetov](https://t.me/t_ruzmetov)\n"
            "• Tel: +998 93 753 75 30"
        )
    elif query.data == "back_to_start":
        await start(update, context)
        return

    try:
        await query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Xatolik: {e}")
        await query.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

# Agar foydalanuvchi matn yozsa
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📋 Menyuni ochish", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Iltimos, kerakli bo'limni tanlash uchun quyidagi tugmani bosing:", 
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("Bot muvaffaqiyatli ishga tushdi!")
    application.run_polling()

if __name__ == "__main__":
    main()