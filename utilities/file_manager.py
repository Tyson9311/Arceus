import os
from config import Config

def save_uploaded_file(file, user_id, file_name):
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(Config.UPLOAD_FOLDER, f"{user_id}_{file_name}")
    
    with open(file_path, 'wb') as f:
        file.download(out=f)
    
    return file_path
