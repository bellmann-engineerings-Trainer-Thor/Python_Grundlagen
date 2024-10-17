# Klasse


class Pizza:

    def __init__(self, bratwurst="Salami", durchmesser=15):
        self.belag = bratwurst
        self.durchmesser = durchmesser

    def info(self):
        print(f"Ich bin eine Pizza! Mein belag ist: {self.belag}, mein Durchmesser ist: {self.durchmesser}")

    def liefern(self, adresse):
        print(f"Bin unterwegs! Ziel: {adresse}")

pizza1 = Pizza()
# pizza2 = Pizza("Fungi", 48)

pizza1.info()
print(pizza1.info())
# pizza2.info()

# print("liefern() aufrufen")
# pizza1.liefern("Wegelagererstraße")     # Bin unterwegs! Ziel: Wegelagererstraße
# pizza2.liefern("Hinterm Sofa")          # Bin unterwegs! Ziel: Hinterm Sofa