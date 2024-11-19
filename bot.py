from ultralytics import YOLO
import pyautogui
import os
import time


def take_screenshot():
    dir = "live"
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(dir, "screenshot-live.png"))
    print("[!] Took screenshot")


def get_midpoints():
    midpoints = []
    model = YOLO("best-ao.pt")
    results = model.predict("live/screenshot-live.png", conf=0.6, save=True)

    boxes = results[0].boxes.xyxy.tolist()

    for box in boxes:
        mid_x = (box[0] + box[2]) / 2
        mid_y = (box[1] + box[3]) / 2

        midpoints.append((mid_x, mid_y))

    return midpoints


def main():
    print("[!] Program Initializing.")

    while True:
        take_screenshot()
        midpoints = get_midpoints()
        pyautogui.click(midpoints[0][0], midpoints[0][1])
        
        time.sleep(13) # Wait to finish mining, adjust this accordingly.


if __name__ == "__main__":
    main()
