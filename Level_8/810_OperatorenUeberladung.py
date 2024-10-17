class Zahl:
    def __init__(self, wert):
        self.wert = wert

    # Überladung des Additionsoperators (+)
    def __add__(self, other):
        if isinstance(other, Zahl):
            return Zahl(self.wert + other.wert)
        else:
            return Zahl(self.wert + other)

    # Überladung des Subtraktionsoperators (-)
    def __sub__(self, other):
        if isinstance(other, Zahl):
            return Zahl(self.wert - other.wert)
        else:
            return Zahl(self.wert - other)

    # Überladung des Gleichheitsoperators (==)
    def __eq__(self, other):
        if isinstance(other, Zahl):
            return self.wert == other.wert
        return False

    # Überladung der String-Repräsentation (str)
    def __str__(self):
        return f"Zahl({self.wert})"

# Beispiele
z1 = Zahl(5)
z2 = Zahl(3)
z3 = z1 + z2
print(z3)  # Ausgabe: Zahl(8)

z4 = z1 - 2
print(z4)  # Ausgabe: Zahl(3)

print(z1 == z2)  # Ausgabe: False
print(z1 == Zahl(5))  # Ausgabe: True
