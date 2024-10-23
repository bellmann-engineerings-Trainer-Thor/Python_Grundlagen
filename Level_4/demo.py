


meineListe = [1, 5, 2, 3, 4, 5, "string", True]
print(meineListe)
print(type(meineListe))



print("Länge der Liste aufrufen")
laenge = len(meineListe)
print(laenge)           # 8
print(len(meineListe))  # 8



print("Zugriff auf ein einzelnes element der Liste")
element = meineListe[7]
print(element)


print("Einzelnes element verändern")
meineListe[2] = "hallo Welt!"
print(meineListe)       # [1, 5, 'hallo Welt!', 3, 4, 5, 'string', True]
print(meineListe[2])


print("Element zur Liste hinzufügen")
meineListe.append(42)
print(meineListe)



print("Element an einer bestimmten Stelle der Liste hinzufügen")
meineListe.insert(0,99)
print(meineListe)


# achtung veraltet
print("Element aus der Liste entfernen")
meineListe.remove("string")
# meineListe.remove("string646") # ValueError: list.remove(x): x not in list
print(meineListe)


print("Element an spezifischer Position entfernen und zurückgeben")
entferntes_element = meineListe.pop(0)
meineListe.pop(0)
print(f"entferntes_element = {entferntes_element}") # entferntes_element = 99
print(meineListe)


print("Element mit del entfernen")
del meineListe[1]
print(meineListe)


print("Prüfen, ob ein Element in der Liste ist")
ist_enthalten = 42 in meineListe
print(ist_enthalten)    # True
print(8 in meineListe)  # False


print("Alle Elemente aus der Liste entfernen")
meineListe.clear()
print(meineListe)