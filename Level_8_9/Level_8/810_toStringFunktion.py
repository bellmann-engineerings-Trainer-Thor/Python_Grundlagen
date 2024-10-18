class Zahl:
    def __init__(self, wert):
        self.wert = wert

    def __str__(self):
        return f"mein wert ist: {self.wert}"


zahl1 = Zahl(5)
print(zahl1)

