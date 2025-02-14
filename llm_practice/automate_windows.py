import pyautogui
import keyboard
import time

def open_start_menu():
    """Simulate pressing the Windows key to open the Start menu."""
    pyautogui.press('win')
    time.sleep(1)  # Allow time for the menu to open

def search_in_start_menu(query):
    """Open the Start menu and type a search query."""
    open_start_menu()
    pyautogui.typewrite(query, interval=0.1)
    pyautogui.press('enter')

def open_file_explorer():
    """Open File Explorer using Windows+E shortcut."""
    pyautogui.hotkey('win', 'e')

def minimize_all_windows():
    """Minimize all windows using Windows+D shortcut."""
    pyautogui.hotkey('win', 'd')

def lock_computer():
    """Lock the computer using Windows+L shortcut."""
    pyautogui.hotkey('win', 'l')

def main():
    print("Automating Windows Key Operations...")
    time.sleep(2)  # Give user time to prepare

    # Open Start menu and search for Notepad
    print("Searching for Notepad...")
    search_in_start_menu("Notepad")
    time.sleep(3)

    # Open File Explorer
    print("Opening File Explorer...")
    open_file_explorer()
    time.sleep(3)

    # Minimize all windows
    print("Minimizing all windows...")
    minimize_all_windows()
    time.sleep(3)

    # Lock the computer
    print("Locking the computer...")
    lock_computer()

if __name__ == "__main__":
    #main()
    lock_computer()
