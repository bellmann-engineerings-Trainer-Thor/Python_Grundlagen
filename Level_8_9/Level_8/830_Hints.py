from typing import List, Dict, Set, Tuple, Optional

zahl: int = True
print(type(zahl))

# Primitive Typen
zahl: int = 8
fließkommazahl: float = 5.5
zeichenkette: str = "Hallo Welt"
wahrheitswert: bool = True
wahrheitswert: bool = "saöjoghnaüusofg"


# Collection Typen mit spezifischen Elementtypen
zahl_liste: List[int] = [1, 2, 3, 4, 5, "asd"]
zeichenkette_set: Set[str] = {"Alice", "Bob", "Charlie"}
schluessel_wert_paare: Dict[str, int] = {"Alice": 30, "Bob": 25}
gemischtes_tuple: Tuple[int, str, bool] = (1, "Zwei", False)
#
# Methoden
def addiere(zahl1: int, zahl2: int) -> int:
    return zahl1 + zahl2

def begruessung(name: str) -> str:
    return f"Hallo, {name}!"

def liste_hinzufuegen(liste: List[int], element: int) -> List[int]:
    liste.append(element)
    return liste

