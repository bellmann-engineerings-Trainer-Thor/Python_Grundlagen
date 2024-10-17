# enhanced for loop
# iteriert ohne Index durch den gesamte Collection

print("Iteration über ein Tupel")
tupel = (1, 2, 3)
for bratwurst in tupel:
    print(bratwurst)

print("Iteration über eine Liste")
liste = [4, 5, 6]
for element in liste:
    print(element)
#
print("Iteration über ein Set")
menge = {7, 8, 9}
for element in menge:
    print(element)
#
print("Iteration über ein Dictionary")
dictionary = {'a': 1, 'b': 2, 'c': 3}
for key, value in dictionary.items():
    print(f"{key}: {value}")

