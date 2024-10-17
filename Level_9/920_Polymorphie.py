class Tier:
    def sprechen(self):
        print("ich bin ein Tier")

class Hund(Tier):
    def sprechen(self):
        print("Wuff!")

class Katze(Tier):
    def sprechen(self):
        print("Miau!")

tiere = [Hund(), Katze()]

for tier in tiere:
    tier.sprechen()  # Die Methode 'sprechen' verhält sich je nach Objekttyp unterschiedlich

