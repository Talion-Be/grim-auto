# main.py

import time
import pyautogui

def move_to(x, y):
    print(f"Déplacement vers ({x}, {y})")
    pyautogui.moveTo(x, y)
    pyautogui.click()

if __name__ == "__main__":
    time.sleep(3)  # Temps pour revenir dans la fenêtre de jeu

    positions = [
        (800, 400),
        (900, 500),
        (1000, 600)
    ]

    for pos in positions:
        move_to(*pos)
        time.sleep(1.5)  # Temps pour que le perso se déplace
