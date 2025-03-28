import pyautogui
import time
import keyboard

# Coordonnées des positions à cliquer (tu peux les ajuster)
positions = [(100, 200), (300, 400), (500, 600)]

print("✅ Appuie sur la touche F2 pour commencer.")
keyboard.wait("F2")  # Attend que tu appuies sur F2

print("🚀 Script lancé. Appuie sur 'Esc' pour arrêter.")

while True:
    if keyboard.is_pressed("esc"):
        print("🛑 Script arrêté.")
        break

    for x, y in positions:
        print(f"➡️ Clique en ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(1)  # Attendre 1 seconde entre les clics
