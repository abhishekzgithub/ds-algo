import pyautogui
import time

def lock_screen():
    # Simulate pressing the Windows key + L to lock the screen
    pyautogui.hold('win')
    pyautogui.press('L')

if __name__ == "__main__":
    print("Locking the screen in 5 seconds...")
    #time.sleep(5)  # Wait for 5 seconds before locking the screen
    lock_screen()
    print("Screen locked.")