# Tupel

meinTupel = (1, 5, 2, 3, 4, 5, "string", True)
print(meinTupel)      # (1, 5, 2, 3, 4, 5, 'string', True)


print("Länge des Tupels aufrufen")
laenge = len(meinTupel)
print(laenge)         # 8
print(len(meinTupel)) # 8

print("Zugriff auf ein einzelnes Element im Tupel")
element = meinTupel[0]
print(element)        # 1
print(meinTupel[7])   # True

# Achtung: Tupel sind unveränderlich, daher können Elemente nicht direkt geändert werden
print("Versuch, ein einzelnes Element zu ändern (nicht möglich)")
# meinTupel[2] = "hallo Welt!" # TypeError: 'tuple' object does not support item assignment
# print(meinTupel)    # (1, 5, 2, 3, 4, 5, 'string', True)

print("Prüfen, ob ein Element im Tupel ist")
ist_enthalten = 42 in meinTupel
print(ist_enthalten)  # False
print(5 in meinTupel) # True

print("Versuch, den Tupel zu leeren (nicht möglich)")
meinTupel.clear()
print(meinTupel)    # (1, 5, 2, 3, 4, 5, 'string', True)

