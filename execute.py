 The keyboard module in Python provides access to all keys on your local machine. Here's an example of how you can use it to control a screen:
import keyboard
def lock_screen():
    "Locks the computer screen."
    keyboard.write("Lock screen")  # This command will be entered using the keyboard module

lock_screen()