"""***********************************************************
Python print()-Funktion und ihre benannten Parameter
***********************************************************"""


"""***********************************************************
sep: Definiert das Trennzeichen zwischen den Ausgaben.
Standardmäßig ist dies ein Leerzeichen.
***********************************************************"""
# print("sep")
#
print("Hallo", "Welt")  # Hallo Welt (Default)
print("Hallo", "Welt", sep=" ")  # Hallo Welt (Default)
print("Hallo", "Welt", sep="-")  # Hallo-Welt
print("Hallo", "Welt", sep="#")  # Hallo#Welt

# """***********************************************************
# end: Definiert, was am Ende der Ausgabe hinzugefügt wird.
# Standardmäßig ist dies ein Zeilenumbruch.
# ***********************************************************"""
# print("end")
# print("Hallo", end="\n") # (Default)
# print("Welt")
# print("Hallo", end=" ")
# print("Welt")
# print("Hallo", end="")
# print("Welt")
#
# # Kombination von 'sep' und 'end': Nutzt beide Parameter in einem Befehl
# print("kombination")
# print("Hallo", "schöne", "neue", "Welt", sep="-", end="!")