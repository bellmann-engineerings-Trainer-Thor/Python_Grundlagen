# Passwortqualität
#
# Schreibe eine Funktion, die die Qualität von Passwörtern nach
# einem einfachen Punktesystem bewertet.
# Es gelten dabei die folgenden
# Regeln:
# – Passwort mit 7 oder weniger Zeichen: immer 0 Punkte,
#   egal, welche Kriterien noch erfüllt sind.
# – Ab 8 Zeichen: 1 Punkt
# – Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
# – Enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
# – Enthält zumindest eine Ziffer: +1 Punkt
# – Enthält zumindest ein Sonderzeichen: +1 Punkt
#
# Beispiele:
# – 'abc': 0 Punkte
# – 'abcdefghij': 2 Punkte
# – 'ab1122$$!!': 3 Punkte
# – 'Abcd1234$!': 5 Punkte
