# print("while-Schleife")
# i = 0
# while i < 5:
#     print(i)
#     i += 1


# print("unendliche while-Schleife")
# while True:
#     print("läuft noch")


print("nested while-Schleife")
outer = 0
inner = 0

while outer < 5:
    print("outer =", outer)
    while inner < 5:
        print("inner =", inner)
        inner += 1
    outer += 1
    inner = 0

print("Beispiel String Manipulation")
i = 0
myString = "|"
while i < 10:
    print(myString)
    myString += "|"
    i += 1

