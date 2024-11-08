# Dictionary

meinDictionary = {"name": "Max", "alter": 30, "stadt": "Berlin", "beruf": "Lehrer"}
print(meinDictionary)  # {'name': 'Max', 'alter': 30, 'stadt': 'Berlin', 'beruf': 'Lehrer'}


print("Länge des Dictionaries aufrufen")
laenge = len(meinDictionary)
print(laenge)          # 4
print(len(meinDictionary)) # 4

print("Zugriff auf ein einzelnes Element im Dictionary")
element = meinDictionary["name"]
print(element)         # Max
print(meinDictionary["beruf"])  # Lehrer

print("Einzelnes Element im Dictionary verändern")
meinDictionary["alter"] = 35
print(meinDictionary)  # {'name': 'Max', 'alter': 35, 'stadt': 'Berlin', 'beruf': 'Lehrer'}

print("Neues Element zum Dictionary hinzufügen")
meinDictionary["hobby"] = "Fahrradfahren"
print(meinDictionary)  # {'name': 'Max', 'alter': 35, 'stadt': 'Berlin', 'beruf': 'Lehrer', 'hobby': 'Fahrradfahren'}

print("Element aus dem Dictionary entfernen")
entferntes_element = meinDictionary.pop("stadt")
print(f"entferntes_element = {entferntes_element}")  # entferntes_element = Berlin
print(meinDictionary)  # {'name': 'Max', 'alter': 35, 'beruf': 'Lehrer', 'hobby': 'Fahrradfahren'}

print("Überprüfen, ob ein Schlüssel im Dictionary vorhanden ist")
ist_enthalten = "name" in meinDictionary
print(ist_enthalten)  # True
print('Max' in meinDictionary)  # False

print("Alle Schlüssel-Wert-Paare durchlaufen")
for schluessel, wert in meinDictionary.items():
    print(f"{schluessel}: {wert}")

print("Alle Elemente aus dem Dictionary entfernen")
meinDictionary.clear()
print(meinDictionary)  # {}
