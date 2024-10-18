class Maschiene(object):
    counter = 0

    def __init__(self):
        Maschiene.counter += 1
        self.typ = "Maschiene"
        self.id = Maschiene.counter
        self.isActive = False

    def __str__(self):
        return f"{self.typ}(id: {self.id} isActive: {self.isActive})"

class Roboter(Maschiene):
    def __init__(self):
        super().__init__()
        self.typ = "Roboter"


class Androide(Roboter):

    def __init__(self):
        super().__init__()
        self.typ = "Androide"

    def walk(self):
        print("roboter läuft")
class Drone(Maschiene):

    def __init__(self):
        super().__init__()
        self.typ = "Androide"

    def fliegen(self):
        print("Drone fliegt")

tier1 = Maschiene()
hund1 = Roboter()
katze1 = Androide()
katze = Drone()


maschienen = [tier1, hund1, katze1, katze]

for m in maschienen:
    m.isActive = True
    print(m)

for m in maschienen:
    m.walk()

# # tier1.sprechen()
# # hund1.sprechen()
# # katze1.sprechen()
#
#
# tiere = [tier1, hund1, katze1, Tier(), Hund(), Katze(), True, "String", 1, 5.8]
# for tier in tiere:
#     tier.sprechen()
# #
# # objekte = [tier1, hund1, katze1, Tier(), Hund(), Katze(), True, "String", 1, 5.8]
# # for objekt in objekte:
# #     print(objekt)
#
#


