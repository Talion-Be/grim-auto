import mouse

coordonnees = []

def record_click(event):
    if isinstance(event, mouse.ButtonEvent) and event.event_type == mouse.DOWN:
        x, y = mouse.get_position()  # récupère la position actuelle du curseur
        coordonnees.append((x, y))
        print(f"Clic enregistré à : {x}, {y}")

print("Enregistrement démarré. Appuie sur ESC pour terminer.")

mouse.hook(record_click)
mouse.wait(button='esc')  # ESC pour arrêter

# Sauvegarde dans un fichier
with open("coordonnees.txt", "w") as f:
    for x, y in coordonnees:
        f.write(f"{x},{y}\n")

print("Enregistrement terminé.")
