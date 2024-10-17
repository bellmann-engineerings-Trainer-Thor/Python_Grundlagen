# Zwei Zahlen genau vergleichen
#
# Schreibe ein Programm, das zwei zufällige Zahlen erzeugt.
# Dann soll das Programm testen und ausgeben,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.

import random
zahl1 = random.random()
zahl2 = random.random()
print(f"{zahl1} ist größer als {zahl2}"
      if zahl1 > zahl2
      else f"{zahl2} ist größer als {zahl1}"
      if zahl2 > zahl1
      else f"{zahl1} und {zahl2} sind gleich groß")



# TrueCase if Boolean else FalseCase

ergebnis = ""
if (zahl1 < zahl2):
    ergebnis = "zahl1 ist kleiner"
else:
    ergebnis = "zahl1 ist größer"

ergebnis = "zahl1 ist kleiner" if zahl1 < zahl2 else "zahl1 ist größer"



