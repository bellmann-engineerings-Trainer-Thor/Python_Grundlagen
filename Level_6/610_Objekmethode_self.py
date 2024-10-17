# Objektmethoden und self

class Pizza:
    def __init__(self, belag="Salami", durchmesser=15):
        self.belag = belag
        self.durchmesser = durchmesser

    def info(self):
        print(f"Ich bin eine Pizza! Mein belag ist: {self.belag}, mein Durchmesser ist: {self.durchmesser}")

    def liefern(self, adresse):
        print(f"Bin unterwegs! Ziel: {adresse}")



print("Objekt erstellen")
pizza1 = Pizza()
pizza2 = Pizza("Fungi", 48)

print("info() aufrufen")
pizza1.info()                           # Ich bin eine Pizza! Mein belag ist: Salami, mein Durchmesser ist: 15
pizza2.info()                           # Ich bin eine Pizza! Mein belag ist: Fungi, mein Durchmesser ist: 48

print("liefern() aufrufen")
pizza1.liefern("Wegelagererstraße")     # Bin unterwegs! Ziel: Wegelagererstraße
pizza2.liefern("Hinterm Sofa")          # Bin unterwegs! Ziel: Hinterm Sofa
