from telegram import Update
from telegram.ext import CallbackContext
from utilities import file_manager
import os

def start_hosting(update: Update, context: CallbackContext):
    context.user_data['hosting'] = True
    update.message.reply_text(
        "🚀 नया बॉट होस्ट करें\n\n"
        "कृपया अपनी बॉट फाइल (ZIP या .py) अपलोड करें"
    )

def handle_upload(update: Update, context: CallbackContext):
    if 'hosting' not in context.user_data:
        return
    
    file = update.message.document
    if not file:
        update.message.reply_text("❌ कोई फाइल नहीं मिली!")
        return
    
    file_name = file.file_name
    if not any(file_name.endswith(ext) for ext in Config.ALLOWED_EXTENSIONS):
        update.message.reply_text("❌ अमान्य फाइल फॉर्मेट! सिर्फ ZIP/PY फाइल्स")
        return
    
    saved_path = file_manager.save_uploaded_file(file, update.effective_user.id, file_name)
    update.message.reply_text(f"✅ फाइल सेव हुई: {saved_path}\nअब /setup कमांड का उपयोग करें")
