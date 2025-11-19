# Save this as find_coordinates.py
import pyautogui
import time

print("Mouse Position Tracker")
print("Move mouse to corners of Google Chat window and note coordinates:")
print("Press Ctrl+C to exit")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone!")