# Funktionen auch Methoden genannt


print("Funktion ohne Rückgabewert")
def gruessen():
    print("Hallo Welt!")

print("Methoden-Aufruf: gruessen()")
gruessen()



print("Funktion mit Rückgabewert")
def summe(a, b):
    return a + b
ergebnis = summe(5, 3)
print("summe(5, 3)", summe(5, 3))
print("Methoden-Aufruf: ergebnis = summe(5, 3)", ergebnis)




print("Funktion mit named Parametern")
def vollstaendiger_name(vorname, nachname = "nix"):
    return vorname + " " + nachname

print(vollstaendiger_name("John", "Doe"))
print(vollstaendiger_name("John"))
print(vollstaendiger_name(nachname="John", vorname="Doe"))




print("Funktion mit variadischen Argumenten (beliebig viele Argumente)")
def summe_aller(*zahlen):
    return sum(zahlen)
summe_aller_parameter = summe_aller(1, 2, 3, 4, 5)
print("summe_aller(1, 2, 3, 4, 5)", summe_aller(1, 2, 3, 4, 5))




print("Funktion mit Keyword-Argumenten (Schlüsselwort-Argumente)")
def person_info(**info):
    for schluessel, wert in info.items():
        print(f"{schluessel}: {wert}")
person_info(Name="John", Alter=30, Beruf="Ingenieur")
