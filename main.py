# main.py
import pyautogui
import time

print("Déplacement de la souris dans 3 secondes...")
time.sleep(3)
pyautogui.moveTo(1000, 500, duration=1)
pyautogui.click()
print("Clic effectué.")