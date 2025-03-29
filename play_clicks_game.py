import mouse
import time

print("Démarrage dans 5 secondes...")
time.sleep(5)

with open("coordonnees.txt", "r") as f:
    for line in f:
        x, y = map(int, line.strip().split(","))
        print(f"Clic à : {x}, {y}")
        mouse.move(x, y, absolute=True, duration=0.1)
        mouse.click()
        time.sleep(0.5)
