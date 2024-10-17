class Auto:
    def __init__(self, maxSpeed):
        self.__maxSpeed = maxSpeed  # Der Setter wird aufgerufen

    @property
    def maxSpeed(self):
        """Getter-Methode für maxSpeed"""
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, value):
        """Setter-Methode für maxSpeed"""
        if value < 0:
            print("Die Geschwindigkeit darf nicht negativ sein.")
            return
        self.__maxSpeed = value

auto = Auto(50)

# nutzen des Setters
auto.maxSpeed = 100
auto.maxSpeed = -100
# auto.maxSpeed(100)
# auto.maxSpeed(200)
wert = auto.maxSpeed = 100

# nutzen des Getters
print(auto.maxSpeed)  # Ausgabe: 100

