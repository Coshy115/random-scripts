# Python 3.14.2
# Go to https://spinquest.com/casino/games/iconic21_launch_spq_mines and set grid size to 4x4 and mines to 1
# Set up for window on second left monitor with resolution 1920x1080, fullscreen, 100% zoom, bookmarks bar visible
# For single monitor, unsign x coordinates and subtract x from 1920

import pyautogui
import time
import os

refresh_button = -1830, 59
play_button = -941, 587
auto_button = -1268, 313
amount_entry = -1411, 394 # needs double-clicked
bet_amount = "0.1"
first_square = -955, 385
autoplay_button = -1349, 652 

def countdown(text, t):
    while t:
        timer = text + ': {:-}'.format(t)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def main():
    os.system("cls")
    countdown("Starting in", 5)
    while True:
        os.system("cls")
        print("\nRefreshing page...")
        pyautogui.click(refresh_button)
        time.sleep(20)
        print("Clicking play...")
        pyautogui.click(play_button)
        time.sleep(1)
        print("Setting mode to 'auto'...")
        pyautogui.click(auto_button)
        time.sleep(1)
        print("Changing bet amount to 0.1...")
        pyautogui.doubleClick(amount_entry)
        pyautogui.typewrite(bet_amount)
        time.sleep(2)
        print("Clicking first square...")
        pyautogui.click(first_square)
        pyautogui.click(first_square)
        time.sleep(1)
        print("Starting autoplay...")
        pyautogui.click(autoplay_button)
        print("Refreshing in 30 minutes...")
        time.sleep(1795)

if __name__ == "__main__":
    main()