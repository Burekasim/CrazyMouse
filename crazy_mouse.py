import pyautogui
import time
import random


if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    while True:
        random_time = random.randint(0, 12)
        time.sleep(random_time)
        random_x = random.randint(-30, 30)
        random_y = random.randint(-30, 30)
        duration = random.randint(2, 6)
        pyautogui.dragRel(random_x, random_y, duration=duration)