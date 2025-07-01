import os
import pyautogui


def capturar_tela():
    os.makedirs("screenshot", exist_ok=True)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot/top.png")