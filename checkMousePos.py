import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")  # Print on the same line
    time.sleep(0.1)  # Adjust the sleep time as needed