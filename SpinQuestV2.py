# Python 3.14.2
# Search for image of play button under overlay after refresh and wait for that to click play, otherwise, wait 20 seconds

import pyautogui
import time
import os

os.system("cls")

input("Place mouse over refresh button and press ENTER...")
refresh_button = pyautogui.position().x, pyautogui.position().y
input("Place mouse over play button in center of screen and press ENTER...")
play_button = pyautogui.position().x, pyautogui.position().y
input("Place mouse over amount field and press ENTER...")
amount_field = pyautogui.position().x, pyautogui.position().y
input("Place mouse over auto button and press ENTER...")
auto_button = pyautogui.position().x, pyautogui.position().y
input("Place mouse over square and press ENTER...")
square = pyautogui.position().x, pyautogui.position().y
input("Place mouse over autoplay button and press ENTER...")
autoplay_button = pyautogui.position().x, pyautogui.position().y

print("Starting script...")
time.sleep(1)

def refresh_in_thirty():
    for i in range(29, 1, -1):
        if i == 1:
            print("Refreshing in" + f": {i} minute  ", end="\r")
        else:
            print("Refreshing in" + f": {i} minutes ", end="\r")
        time.sleep(60)
    else:
        for j in range(60, -1, -1):
            if j == 1:
                print("Refreshing in" + f": {j} second  ", end="\r")
            else:
                print("Refreshing in" + f": {j} seconds ", end="\r")
            time.sleep(1)

def main():
    os.system("cls")
    time.sleep(1)

    print("Refreshing the page...")
    pyautogui.click(refresh_button)
    time.sleep(10)

    print("Clicking the play button...")
    pyautogui.click(play_button)
    time.sleep(1)

    print("Entering the bet amount...")
    pyautogui.click(amount_field)
    pyautogui.typewrite("0.1")

    print("Switching to auto mode...")
    pyautogui.click(auto_button)

    print("Selecting a square...")
    pyautogui.moveTo(square, duration=0.5)
    pyautogui.click(square)

    print("Pressing the autoplay button...")
    pyautogui.click(autoplay_button)

    refresh_in_thirty()

if __name__ == "__main__":
    while True:
        main()