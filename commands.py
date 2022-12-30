import pyautogui
import time
import keyboard
import mouse

print("Print button left/right")
wbutton = input()

def click():
    mouse.click(button=f'{wbutton}')

click()
