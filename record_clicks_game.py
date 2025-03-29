import mouse
import keyboard

coordonnees = []
running = True

def record_click(event):
    if isinstance(event, mouse.ButtonEvent) and event.event_type == mouse.DOWN:
        x, y = mouse.get_position()
        coordonnees.append((x, y))
        print(f"Clic enregistré à : {x}, {y}")

def stop_recording(event):
    global running
    running = False
    print("Arrêt de l'enregistrement demandé par ESC.")

print("Enregistrement démarré. Appuie sur ESC pour terminer.")

# Démarre l'écoute souris
mouse.hook(record_click)

# Écoute de la touche ESC pour stopper
keyboard.on_press_key("esc", stop_recording)

# Boucle active jusqu'à ESC pressé
while running:
    pass

# Arrêt propre des hooks
mouse.unhook_all()
keyboard.unhook_all()

# Sauvegarde les clics dans un fichier
with open("coordonnees.txt", "w") as f:
    for x, y in coordonnees:
        f.write(f"{x},{y}\n")

print("Enregistrement terminé.")
