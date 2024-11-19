import os
import pyautogui
import time
import keyboard

""" Used for data collection """

def take_screenshot():
    data_dir = "data"
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(data_dir, f"screenshot-{timestamp}.png"))


if __name__ == "__main__":
    # Take screenshot whenever 'q' is pressed.
    while True:
        keyboard.wait("q")
        take_screenshot()
        print("Took screenshot")

