# Globale Variablen sind außerhalb von Funktionen definiert und können im gesamten Programm verwendet werden.
globale_variable = "Ich bin global"

# def beispiel_funktion():
#     print("hier wird beispiel_funktion() ausgeführt")
#     # Lokale Variable, nur innerhalb dieser Funktion gültig.
#     lokale_variable = "Ich bin lokal"
#     print(lokale_variable)  # Gibt die lokale Variable aus.
#     print(globale_variable)  # Zugriff auf die globale Variable ist auch möglich.
# beispiel_funktion()

# print("Zugriff auf die lokale Variable außerhalb ihrer Funktion führt zu einem Fehler.")
# # print(lokale_variable)  # Fehler: lokale_variable ist nicht definiert.
#
# #
# # Demonstration der Schattenbildung
# def schatten_funktion():
#     print("hier wird schatten_funktion() ausgeführt")
#     globale_variable = "Lokal überschrieben"
#     print(globale_variable)  # Gibt die neu zugewiesene "lokale" Variable aus, überschattet die globale.
#
# schatten_funktion()
# print(globale_variable)  # Gibt die ursprüngliche globale Variable aus, da die lokale Variable nur in schatten_funktion existiert.
# #
# #
# #
# def nichtMehrSchatten_funktion():
#     print("hier wird nichtMehrSchatten_funktion() ausgeführt")
#     global globale_variable
#     # globale_variable = "Lokal überschrieben"
#     print(globale_variable)  # Gibt die neu zugewiesene "lokale" Variable aus, überschattet die globale.
#
# nichtMehrSchatten_funktion()
# print(globale_variable)
