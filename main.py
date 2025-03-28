# Netbox Deployment (fichier actuel)
import pyautogui
import time
import keyboard

positions = []

print("📍 Mode enregistrement activé.")
print("➡️ Appuie sur F8 pour enregistrer une position.")
print("✅ Appuie sur F9 pour terminer l'enregistrement.")

while True:
    if keyboard.is_pressed("F8"):
        pos = pyautogui.position()
        positions.append(pos)
        print(f"💾 Position enregistrée: {pos}")
        time.sleep(0.3)  # Anti double clic

    if keyboard.is_pressed("F9"):
        print("🛑 Enregistrement terminé.")
        break

print("\n📌 Liste des positions enregistrées :")
for i, (x, y) in enumerate(positions, 1):
    print(f"{i}. ({x}, {y})")
