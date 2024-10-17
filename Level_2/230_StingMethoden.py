# String Methoden

myString = "Hello World!"
print("len(myString)")
# gibt die Laenge des Strings zurueck
laenge = len(myString)
print(laenge) #12

print("einzelner Buchstabe (Substring)")
print("einzelner_Buchstabe = myString[5]")
einzelner_Buchstabe = myString[2] # exclusive des 5.-Index Hallo
print(einzelner_Buchstabe) # l

print("String- Teilung (Substring)")
print("erster_teil = myString[:5]")
erster_teil = myString[:5] # exclusive des 5.-Index Hallo
print(erster_teil) # Hallo


print("zweiter_teil = myString[6:] (Substring)")
zweiter_teil = myString[6:] # inklusive des 6.-Index
print(zweiter_teil) # World!

print("teil_ab_index_bis_index = myString[3:8]")
teil_ab_index_bis_index = myString[3:8] # erster index ist inklusive der zweite ist exclusive
print(teil_ab_index_bis_index)

print("myString.upper()")
gross = myString.upper() # Methoden-Aufruf
print(gross) # HALLO WELT

print("myString.lower()")
klein = myString.lower()
print(klein) # hallo welt

print("myString.replace('World', 'Python')")
ersetzt1 = myString.replace("World", "Python")
print(ersetzt1) # Hallo Python

mein_anderer_string = "Otto oder Anna"

print('mein_anderer_string.replace("o", "i", 1)')
ersetzt1 = mein_anderer_string.replace("o", "i", 1)
print(ersetzt1)

print('mein_anderer_string.replace("o", "i")')
ersetzt2 = mein_anderer_string.replace("o", "i")
print(ersetzt2)

print('myString.find("World")')
position = myString.find("World") # gibt den Index zurueck bei dem das Wort anfängt
print(position) # 6

print('myString.find("d")')
position = myString.find("d") # gibt den ersten Treffer zurueck
print(position) # 10
print('mein_anderer_string.find("d")')
position1 = mein_anderer_string.find("o") # gibt den ersten Treffer zurueck
print(position1) # 3





