import mouse

coordonnees = []

def record_click(event):
    if isinstance(event, mouse.ButtonEvent) and event.event_type == mouse.DOWN:
        coordonnees.append((event.x, event.y))
        print(f"Clic enregistré à : {event.x}, {event.y}")

print("Enregistrement démarré. Appuie sur ESC pour terminer.")

mouse.hook(record_click)
mouse.wait(button='esc')  # Appuie sur ESC pour arrêter l'enregistrement

# Sauvegarde dans un fichier
with open("coordonnees.txt", "w") as f:
    for x, y in coordonnees:
        f.write(f"{x},{y}\n")

print("Enregistrement terminé.")
