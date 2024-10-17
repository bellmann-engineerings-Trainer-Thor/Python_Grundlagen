# Klasse, Konstruktor und Objektattribute

class Pizza:

    def __init__(self, belagParam, durchmesserParam):
        self.belag = belagParam
        self.durchmesser = durchmesserParam


print("Objekt erstellen")
pizza1 = Pizza("Fungi", 48)
print(pizza1)               # <__main__.Pizza object at 0x000001C0755EFB90>

print("Objekt-Attribute ausgeben")
print(pizza1.belag)         # Fungi
print(pizza1.durchmesser)   # 48

print("Objekt-Attribute verändern")
pizza1.belag = "Salami"
pizza1.durchmesser = 30
print(pizza1.belag)         # Salami
print(pizza1.durchmesser)   # 30

print("Einem Objekt ein Attribut anhängen")
pizza2 = Pizza("Quattro Formaggi", 15)
pizza2.temperatur = "heiß"
print("Zustand pizza2:")
print(pizza2.belag)         # Quattro Formaggi
print(pizza2.durchmesser)   # 15
print(pizza2.temperatur)    # heiß

print("Zustand pizza1:")
print(pizza1.belag)         # Salami
print(pizza1.durchmesser)   # 30
print(pizza1.temperatur)    # AttributeError: 'Pizza' object has no attribute 'temperatur'

