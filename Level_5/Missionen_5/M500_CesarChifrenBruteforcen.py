# Cäsar-Chiffre bruteforcen
#
# Schreibe ein Programm, das alle möglichen Lösungen
# eines Cäsar-chiffrierten Strings ausgibt.
#
# Was bedeutet "vxumxgssokxkt sginz yvgyy"?
#
# Wer die Cäsar-Chiffre nicht kennt: https://de.wikipedia.org/wiki/Caesar-Verschlüsselung



def caesar_bruteforce(verschluesselteNachricht):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for shift in range(8):
        entschluesselterText = ''
        for buchstabe in verschluesselteNachricht:
            if buchstabe in alphabet:
                index = alphabet.index(buchstabe)
                shifted_index = (index - shift) % 26
                entschluesselterText += alphabet[shifted_index]
            else:
                entschluesselterText += buchstabe
        print(f"Shift {shift}: {entschluesselterText}")

# Beispieltext entschlüsseln
verschluesselteNachricht = "vxumxgssokxkt sginz yvgyy"
caesar_bruteforce(verschluesselteNachricht)


