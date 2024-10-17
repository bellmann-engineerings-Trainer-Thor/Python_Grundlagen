# Teilersumme
#
# Schreibe eine Funktion, die überprüft, ob bei einer Zahl
# die Summe aller Teiler kleiner als die Zahl ist.
# Die Zahl selbst soll hierbei nicht zu den Teilern zählen.
#
# Bei 81 würde True zurückgegeben werden, da
# 1 + 3 + 9 + 27 = 40
# und 40 < 81
#
# Bei 80 würde False zurückgegeben werden, da
# 1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40 = 106
# und 106 > 80
#
# Beispiel:
# print(pruefe_teilersumme(81))  # True
# print(pruefe_teilersumme(80))  # False
