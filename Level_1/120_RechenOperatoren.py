# Rechenoperatoren
print(3 + 7)  # 10
print(13 - 7)  # 6
print(3 * 7)  # 21
print(21 / 7)  # 3.0

# Bei Division wird immer ein Float zurückgegeben
print(11 / 2)  # 5.5
print(type(10 / 2))  # <class 'float'>

# Sobald eine Fließkommazahl dabei ist, wird ein Float zurückgegeben
print(10.0 * 2)  # 20.0
print(10 * 2.0)  # 20.0
print(10.0 * 2.0)  # 20.0

# Modulo - Restwert-Division
print(9 % 3) # 0
print(10 % 3) # 1
print(11 % 3) # 2
print(2 % 3) # 2

#
print("Zuweisungsoperatoren")
x = 7
print(x + 1)  # 8
print(x)  # x ist immernoch 7
x += 1
print(x)  # jetzt ist x 8

# weitere Zuweisungsoperatoren
x -= 1
x /= 2
x *= 2
x %= 2