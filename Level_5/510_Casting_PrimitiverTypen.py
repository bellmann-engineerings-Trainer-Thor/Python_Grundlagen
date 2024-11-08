# Type-Casting in Python

# Casting ist der Vorgang, bei dem eine Variable von einem Datentyp in einen anderen umgewandelt wird.

## Integer


# Vom String zum Integer
x = "42"
y = int(x)
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>


# Vom Float zum Integer
x = 42.0
y = int(x)
print(y)
print(type(y))  # <class 'int'>


# ACHTUNG: Beim Umwandeln von Float zu Integer wird die Nachkommastelle abgeschnitten!
x = 42.9
y = int(x) # 42
print(type(y))  # <class 'int'>

## Float

# Vom String zum Float
x = "42"
y = float(x)
print(y)  # 42.0
print(type(y))  # <class 'float'>

# Vom Integer zum Float
x = 42
y = float(x)
print(type(y))  # <class 'float'>


## String

# Vom Integer zum String
x = 42
y = str(x)
print(type(y))  # <class 'str'>

# Vom Float zum String
x = 42.0
y = str(x)
print(type(y))  # <class 'str'>


## Boolean

# Vom Integer zum Boolean
x = 1
y = bool(x)
print(y)        # True
print(type(y))  # <class 'bool'>


x = 0
y = bool(x)
print(y)        # False
print(type(y))  # <class 'bool'>

# ACHTUNG: Fast jeder Wert wird zu "False" umgewandelt, außer 1
x = "1"
y = bool(x)
print(y)  # Ausgabe: True  <-- Problem für Anfänger
print(type(y))  # <class 'bool'>

# Vom Boolean zum Integer
x = True
y = int(x)
print(y)  # Ausgabe: 1
print(type(y))  # <class 'int'>

x = False
y = int(x)
print(y)  # Ausgabe: 0
print(type(y))  # <class 'int'>