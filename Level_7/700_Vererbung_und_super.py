# Basisklasse
class Animal:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print(f"{self.name} atmet")

# erbende Klasse
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def waveTail(self):
        print(f"{self.name} wedelt mit dem Schwanz")


animal = Animal("Heinrich")
dog = Dog("Bello")

animal.breath()  # Heinrich atmet
dog.breath()  # Bello atmet

dog.waveTail()
animal.waveTail()
