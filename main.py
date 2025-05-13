from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from core import hosting, security, dashboard
from utilities import database, file_manager
import logging

# लॉगिंग कॉन्फिगरेशन
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🤖 बॉट होस्टिंग सिस्टम में आपका स्वागत है!\n\n"
             "नया बॉट होस्ट करने के लिए /host कमांड का उपयोग करें"
    )

def error(update, context):
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # कमांड हैंडलर
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("host", hosting.start_hosting))
    dp.add_handler(CommandHandler("dashboard", dashboard.show_dashboard))
    
    # फाइल अपलोड हैंडलर
    dp.add_handler(MessageHandler(Filters.document, hosting.handle_upload))
    
    # एरर हैंडलर
    dp.add_error_handler(error)

    updater.start_polling()
    logger.info("बॉट स्टार्ट हो गया है...")
    updater.idle()

if __name__ == "__main__":
    main()
