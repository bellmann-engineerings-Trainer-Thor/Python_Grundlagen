# Set
"""
Veränderbar (mutable)
Kann verschiedene Datentypen enthalten, aber jedes Element muss einzigartig sein (keine Duplikate).
Ungeordnet, d.h., die Reihenfolge der Elemente ist nicht garantiert.
Geeignet für Operationen wie Vereinigung, Schnittmenge, Differenz.
"""

meinSet = {1, 2, 3, 4, 5, 4}
print(meinSet)          # {1, 2, 3, 4, 5}
print("len(meinSet)")
# gibt die Anzahl der Elemente im Set zurück
laenge = len(meinSet)
print(laenge) # 5
#
print("Element zum Set hinzufügen")
print("meinSet.add(6)")
meinSet.add(6) # Fügt das Element 6 zum Set hinzu
print(meinSet) # {1, 2, 3, 4, 5, 6}

print("Mehrere Elemente zum Set hinzufügen")
print("meinSet.update([7, 8, 9])")
meinSet.update([7, 8, 9]) # Fügt mehrere Elemente zum Set hinzu
print(meinSet) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("Element aus dem Set entfernen")
print("meinSet.remove(9)")
meinSet.remove(9) # Entfernt das Element 9 aus dem Set, wirft einen Fehler, wenn das Element nicht existiert
print(meinSet) # {1, 2, 3, 4, 5, 6, 7, 8}

print("Element sicher aus dem Set entfernen")
print("meinSet.discard(8)")
meinSet.discard(8) # Entfernt das Element 8 aus dem Set, kein Fehler, wenn das Element nicht existiert
print(meinSet) # {1, 2, 3, 4, 5, 6, 7}

print("Ein zufälliges Element entfernen")
print("element = meinSet.pop()")
element = meinSet.pop() # Entfernt und gibt ein zufälliges Element zurück
print(element)
print(meinSet)

print("Alle Elemente aus dem Set entfernen")
print("meinSet.clear()")
meinSet.clear() # Entfernt alle Elemente aus dem Set
print(meinSet) # set()

# Prüfen, ob ein Element im Set ist
print("5 in meinSet")
ist_enthalten = 5 in meinSet
print(ist_enthalten) # False

for i in meinSet:
    print(f"Setelement hat den Wert: {i}")
