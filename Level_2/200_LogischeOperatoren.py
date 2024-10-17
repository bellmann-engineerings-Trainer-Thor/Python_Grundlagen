print("Logische Operatoren")
print("and, or, not")

print("and - UND (sowohl als auch)")
print("Nur True, wenn beide True sind")
print(3 >= 2 and 7 != 9)    # True
print(False and True)       # False
print(True and False)       # False
print(False and False)      # False

print("or - ODER (entweder oder)")
print("Nur False, wenn beide False sind")
print(True or True)         # True
print(False or True)        # True
print(True or False)        # True
print(False or False)       # False

print("not - NICHT")
print("not kehrt den Boolean um")
print(not (1 == 1))         # False
print(not True)             # False
print(not False)            # True
