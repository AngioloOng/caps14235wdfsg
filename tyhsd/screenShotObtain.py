import pyautogui
import time
import os

screenshot_folder = "Screenshits"
num_screenshots = 100       # how many screenshots to take
scroll_amount = -520         # negative scroll means scrolling down
delay_between = 2             # seconds between screenshots

print("You have 5 seconds to switch to the document window...")
time.sleep(5)

for i in range(num_screenshots):
    screenshot = pyautogui.screenshot(region=(500, 200, 950, 800))

    filename = os.path.join(screenshot_folder, f"screenshot9_{i+1}.png")
    screenshot.save(filename)
    print(f"Saved {filename}")

    pyautogui.scroll(scroll_amount)
    print("Scrolled down.")
    time.sleep(delay_between)

print("Done capturing screenshots.")
