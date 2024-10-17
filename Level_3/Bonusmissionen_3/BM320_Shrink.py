# Shrink
#
# Die Funktion shrink() soll eine Zeichenkette auf n Zeichen kürzen.
# Für n<15 liefert shrink() einfach die ersten n Zeichen.
# Für größere n sollen die ersten n-10 und die letzten 5 Zeichen
# unverändert erhalten bleiben.
# Dazwischen fügt die Funktion ' ... ' ein.
#
# Schreibe den Code für eine geeignete Funktion
# und sichere die Funktion bestmöglich gegen
# die Übergabe ungültiger oder falscher Parameter ab.
#
# Drei Beispiele illustrieren die Funktionsweise:
# print(shrink("abcdefghijklmnopqrstuvwxyz", 8))    # abcdefgh
# print(shrink("abcdefghijklmnopqrstuvwxyz", 17))   # abcdefg ... vwxyz
# print(shrink("abcdefghijklmnopqrstuvwxyz", 22))   # abcdefghijkl ... vwxyz
