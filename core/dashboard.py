from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utilities import database

def show_dashboard(update: Update, context: CallbackContext):
    user = update.effective_user
    bots = database.get_user_bots(user.id)
    
    keyboard = [
        [InlineKeyboardButton("🔄 रिफ्रेश", callback_data="refresh_dashboard")],
        [InlineKeyboardButton("📊 स्टैट्स", callback_data="show_stats")]
    ]
    
    update.message.reply_text(
        f"👤 यूजर: {user.full_name}\n\n"
        f"🤖 आपके बॉट्स: {len(bots)}\n"
        "नीचे दिए विकल्पों का उपयोग करें:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
