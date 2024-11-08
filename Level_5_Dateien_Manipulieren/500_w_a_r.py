# ******************************************************************
# Schritt 1
# 'w' öffnet/erzeugt eine Datei im (Über-)Schreib-modus / Writemode
# ******************************************************************
with open("Fyle.txt", "w") as datei:
    datei.write("[w] hat den gesamten Text überschrieben")

# ******************************************************************
# Schritt 2
# 'a' öffnet eine Datei im Anhängemodus / Apendmode
# ******************************************************************
with open("Fyle.txt", "a") as datei:
    # Fügt am Ende einer Datei Text hinzu
    datei.write(("\n[a] war auch hier hier! :P"))

# ******************************************************************
# Schritt 3
# 'r' öffnet eine Datei im Lesemodus / Read
# ******************************************************************
with open("Fyle.txt", "r") as datei:
    inhalt = datei.read()
    print(type(inhalt))
    print(f"\t\t\t\t[r] liest: \n{inhalt}")