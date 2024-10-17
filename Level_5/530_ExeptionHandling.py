
#######################################################################################
# Teil 1
#######################################################################################
# print("Ohne Exceptionhandling")
#
# ergebnis = 10 / 0  # <- wirft einen Fehler. Programm stürzt ab
# print("hier sollte das Programm normalerweise weitergehen. Wäre die Exception nicht")


#######################################################################################
# Teil 2
#######################################################################################
# print("try ... except")
# try:
#     # Versuche, durch Null zu teilen, was eine ZeroDivisionError-Exception auslöst
#     ergebnis = 10 / 0
# except ZeroDivisionError:
#     # Diese Zeile wird ausgeführt, wenn eine ZeroDivisionError-Exception auftritt
#     print("Fehler: Division durch Null ist nicht erlaubt!")
#
# print("Dank des Auffangengs der Exeption geht das programm normal weiter")

# #######################################################################################
# # Teil 3
# #######################################################################################
# print("finally")
# try:
#     # Versuche, eine Datei zu öffnen, die möglicherweise nicht existiert, was eine FileNotFoundError auslösen könnte
#     # datei = open("nicht_existierende_datei.txt")
#     # inhalt = datei.read()
#     c = "hallo"
# except FileNotFoundError:
#     # Diese Zeile wird ausgeführt, wenn eine FileNotFoundError-Exception auftritt
#     print("Fehler: Datei wurde nicht gefunden.")
#     ergebnis = 10 / 0
# finally:
#     # Diese Zeile wird immer ausgeführt, egal ob eine Exception aufgetreten ist oder nicht
#     print("Finally-Block wird immer ausgeführt.")
#
# print("Dank des Auffangengs der Exeption geht das programm normal weiter")
# #######################################################################################
# # Teil 4
# #######################################################################################
print("Alle Exceptions")
try:
    # 1. ZeroDivisionError
    ergebnis = 1 / 0
    # 2. FileNotFoundError
    # open('nicht_existierendes_file.txt')
    # 3. ValueError
    int("keineZahl")
    # 4. TypeError
    "2" + 2
    # 5. IndexError
    liste = [1, 2, 3]
    element = liste[5]
    # 6. KeyError
    dict = {"a": 1}
    wert = dict["b"]
    # 7. AttributeError
    None.length()
    # 8. ImportError
    from sys import nicht_existierend
except ZeroDivisionError:
    print(f"Division durch Null.")
except FileNotFoundError:
    print("Datei nicht gefunden.")
except ValueError:
    print("Ungültiger Wert.")
except TypeError:
    print("Typinkompatibilität.")
except IndexError:
    print("Index außerhalb des Bereichs.")
except KeyError:
    print("Schlüssel nicht im Dictionary.")
except AttributeError:
    print("Attribut existiert nicht.")
except ImportError:
    print("Import fehlgeschlagen.")
except Exception as e:
    print(f"Ein anderer Fehler ist aufgetreten: {e}")

# Weitere mögliche Exceptions:
# - NameError: Wenn eine lokale oder globale Name nicht gefunden wird.
# - RuntimeError: Ein Fehler, der nicht in eine spezifische Kategorie fällt.
# - OverflowError: Wenn das Ergebnis einer arithmetischen Operation zu groß ist.
# - SyntaxError: Wenn im Code ein Syntaxfehler vorliegt.
# - IndentationError: Wenn im Code ein Einrückungsfehler vorliegt.
# - AssertionError: Durch eine fehlschlagende assert-Anweisung.
# - KeyboardInterrupt: Wenn der Benutzer die Ausführung unterbricht.
# - MemoryError: Wenn ein Operation wegen Speichermangels nicht abgeschlossen werden kann.
# ... und viele mehr.


# Erklärung:
# - "try": Block, in dem Code ausgeführt wird, der eine Exception auslösen könnte.
# - "except": Fängt eine bestimmte (oder alle) Exceptions auf, die im try-Block aufgetreten sind.
# - "finally": Block, der ausgeführt wird, nachdem die try- und except-Blöcke abgearbeitet wurden, unabhängig davon, ob eine Exception aufgetreten ist oder nicht. Ideal für Aufräumarbeiten.
# - "Exception as e": Eine allgemeine Klasse für Exceptions, die verwendet wird, um alle Exceptions aufzufangen. 'e' enthält die Fehlermeldung der aufgetretenen Exception.
