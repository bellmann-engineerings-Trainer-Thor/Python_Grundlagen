# modul_klasse.py

class MeineKlasse:
    def __init__(self):
        self.nachricht = "Instanz der Klasse wurde erstellt!"

    def ausgabe(self):
        print(self.nachricht)

def main():
    instanz = MeineKlasse()
    instanz.ausgabe()

# Die "name == main"-Syntax sorgt dafür das, dass Skript NICHT ausgeführt wird wenn es importiert wird

if __name__ == "__main__":
    print("Das Skript wird direkt ausgeführt.")
    main()
else:
    print("Das Skript wird als Modul importiert.")
# print("Das Skript wird als Modul importiert.")




# ohne die Syntax wird das Skript ausgeführt, wenn es Importiert wird
# main()


"""
    Daseinsberechtigung und warum diese Syntax sehr beliebt ist, sind:

    Modularität: 
    Man kann denselben Code als Skript ausführen oder als Modul in ein anderes Skript importieren. Beim Importieren 
    werden Codeblöcke innerhalb von if __name__ == "__main__": nicht ausgeführt, was Seiteneffekte verhindert.

    Kontrolle der Ausführung: Es erlaubt, sicherzustellen, dass bestimmte Teile des Codes nur ausgeführt werden, 
    wenn das Skript als Hauptprogramm läuft, und nicht, wenn es als Modul importiert wird.

    Testbarkeit: Man kann einzelne Funktionen und Klassen testen, ohne Code auszuführen, der für die direkte 
    Skriptausführung bestimmt ist.

    Strukturierung: Es hilft, den ausführbaren Teil des Codes vom Definitions-Teil zu trennen, was die Lesbarkeit und 
    Wartbarkeit verbessert.
"""
