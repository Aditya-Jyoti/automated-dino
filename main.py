import pyautogui
import time


ENEMY_COLOUR = 172


def main():
    while True:
        image = pyautogui.screenshot(region=(300, 650, 100, 175)).convert("L")
        data = image.load()

        width, height = image.size
        for x, y in zip(range(width), range(height)):
            if data[x, y] == ENEMY_COLOUR:
                pyautogui.keyDown("up")
                break


if __name__ == "__main__":
    time.sleep(3)
    main()
