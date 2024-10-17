# List

meineListe = [1, 5, 2, 3, 4, 5, "string", True]
print(meineListe)      # [1, 5, 2, 3, 4, 5, 'string', True]


print("Länge der Liste aufrufen")
laenge = len(meineListe)
print(laenge)           # 8
print(len(meineListe))  # 8

print("Zugriff auf ein einzelnes element der Liste")
element = meineListe[0]
print(element)          # 1
print(meineListe[7])    # True

print("Einzelnes element verändern")
meineListe[2] = "hallo Welt!"
print(meineListe)       # [1, 5, 'hallo Welt!', 3, 4, 5, 'string', True]
print(meineListe[2])    # hallo Welt!

print("Element zur Liste hinzufügen")
meineListe.append(42)
print(meineListe)       # [1, 5, 'hallo Welt!', 3, 4, 5, 'string', True, 42]

print("Element an einer bestimmten Stelle der Liste hinzufügen")
meineListe.insert(0,99)
print(meineListe)       # [99, 1, 5, 'hallo Welt!', 3, 4, 5, 'string', True, 42]

# achtung veraltet
print("Element aus der Liste entfernen")
meineListe.remove("string")
# meineListe.remove("string646") # ValueError: list.remove(x): x not in list
print(meineListe)       # [99, 1, 5, 'hallo Welt!', 3, 4, 5, True, 42]

print("Element an spezifischer Position entfernen und zurückgeben")
entferntes_element = meineListe.pop(0)
print(f"entferntes_element = {entferntes_element}") # entferntes_element = 99
print(meineListe)       # [1, 5, 'hallo Welt!', 3, 4, 5, True, 42]

print("Element mit del entfernen")
del meineListe[1]
print(meineListe)       # [1, 'hallo Welt!', 3, 4, 5, True, 42]

print("Prüfen, ob ein Element in der Liste ist")
ist_enthalten = 42 in meineListe
print(ist_enthalten)    # True
print(8 in meineListe)  # False

print("Alle Elemente aus der Liste entfernen")
meineListe.clear()
print(meineListe)       # []