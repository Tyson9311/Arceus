import os

class Config:
    # बेसिक कॉन्फिग
    TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
    ADMINS = [int(id) for id in os.getenv("ADMINS", "123456789").split(",")]
    
    # डेटाबेस कॉन्फिग
    DB_URL = os.getenv("DB_URL", "sqlite:///bots.db")
    
    # होस्टिंग सेटिंग्स
    MAX_STORAGE = int(os.getenv("MAX_STORAGE", 100))  # MB
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "user_uploads")
    ALLOWED_EXTENSIONS = {'zip', 'py'}
