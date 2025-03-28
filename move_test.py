import time
import pyautogui
import pygetwindow as gw

# Cherche la fenêtre du jeu
window = None
for w in gw.getWindowsWithTitle("Grim Dawn"):
    if w.isActive or w.isMaximized or w.isMinimized:
        window = w
        break

if window is None:
    print("❌ Grim Dawn n'est pas ouvert ou la fenêtre n'est pas détectée.")
else:
    print(f"✅ Fenêtre détectée : {window.title}")
    window.activate()
    time.sleep(2)  # Attente après activation

    # Calcule le centre de la fenêtre
    center_x = window.left + window.width // 2
    center_y = window.top + window.height // 2

    print(f"🖱️ Clic au centre de la fenêtre à ({center_x}, {center_y}) dans 3 secondes...")
    time.sleep(3)

    pyautogui.click(center_x, center_y)
    print("✅ Clic effectué !")
