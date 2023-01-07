# Hands-On: Fangen Sie Fehler bei der Generierung von Zufallszahlen ab!
# • Schreiben Sie eine Funktion generate(), die eine Zufallszahl im Interval [0, 1)
# generiert und zuruckgibt. ¨

# Benutzen Sie hierzu die Funktion random() des Moduls random.

# Unmittelbar nach der Generierung der Zufallszahl soll diese am Bildschirm
# ausgegeben werden.

# • Ist die generierte Zufallszahl großer als 0.9, soll (vor Rückgabe der Zahl) eine ¨
# Exception ValueError mit dem Text “Zahl > 0.9 ” geworfen werden.

# • Rufen Sie Ihre Funktion generate() solange auf, bis Sie einen ValueError
# erhalten.

# Geben Sie die entsprechende Exception am Bildschirm aus und
# beenden Sie die Zufallszahlengenerierung.

from random import random


def generate() -> float:
    random_val = random()
    print(random_val)
    if random_val > 0.9:
        raise ValueError("Zahl > 0.9")
    return random_val


while True:
    generate()
