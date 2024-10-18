class Auto:
    def __init__(self, maxSpeed):
        self.__maxSpeed = maxSpeed


    def getMaxSpeed(self):
        return self.__maxSpeed


    @property
    def maxSpeed(self):
        """Getter-Methode für maxSpeed"""
        return self.__maxSpeed

    # def setMaxSpeed(self, newValue):
    #     if newValue < 0:
    #         print("das geht nicht")
    #     else:
    #         self.__maxSpeed = newValue


    @maxSpeed.setter
    def maxSpeed(self, value):
        """Setter-Methode für maxSpeed"""
        if value < 0:
            print("Die Geschwindigkeit darf nicht negativ sein.")
            return self.__maxSpeed = value



auto1 = Auto(200)

# print(auto1.maxSpeed())
print(auto1.maxSpeed)
auto1.maxSpeed = 150
print(auto1.maxSpeed)