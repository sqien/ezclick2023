import pyautogui
import time
import keyboard

cps = int(input("How much clicks do you want? "))
while True:
    def click():
        time.sleep(0.01)
        pyautogui.click()

    def main():
        if keyboard.is_pressed("ctrl + 1"):
            for i in range(cps):
                click()
                if keyboard.is_pressed("ctrl + 2"):
                    exit
    main()
