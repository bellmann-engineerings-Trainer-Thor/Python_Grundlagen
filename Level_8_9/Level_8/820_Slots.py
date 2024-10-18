"""
Verwendung von __slots__ in Python

Normalerweise kann man jeder Instanz einer Klasse in Python beliebig viele neue Attribute zuweisen.
Dies bietet große Flexibilität, führt aber auch zu einem höheren Speicherverbrauch,
da für jede Instanz ein __dict__ angelegt wird, um die Attribute und ihre Werte zu speichern.

Durch Verwendung von __slots__ kann man diese Flexibilität einschränken und den Speicherverbrauch für
Klasseninstanzen reduzieren, indem man festlegt, welche Attribute die Instanzen haben dürfen.

Beispiel:
"""

class Punkt:
    __slots__ = ['x', 'y']  # Definiert, dass Instanzen nur die Attribute x und y haben dürfen

    def __init__(self, x, y):
        self.x = x  # Zuweisung zu einem in __slots__ definierten Attribut ist erlaubt
        self.y = y

# Verwendung der Klasse
punkt = Punkt(1, 2)
print(punkt.x, punkt.y)  # Ausgabe: 1 2

# Versuch, ein nicht erlaubtes Attribut hinzuzufügen
punkt.z = 3  # Würde einen AttributeError auslösen: 'Punkt' object has no attribute 'z'

"""
Vorteile von __slots__:
- Reduzierung des Speicherverbrauchs für Instanzen, da kein __dict__ für jede Instanz angelegt wird.
- Einschränkung der erlaubten Attribute für Instanzen, was zu klarer definierten und möglicherweise sichereren Klassen führt.

Nachteile von __slots__:
- Einschränkung der Flexibilität, da keine zusätzlichen Attribute außer den in __slots__ definierten zugewiesen werden können.
- Erbt eine Klasse von einer anderen Klasse ohne __slots__, wird ein __dict__ angelegt, und der Speichervorteil kann verloren gehen.

Hinweis:
- __slots__ sollte mit Bedacht eingesetzt werden, besonders wenn Flexibilität eine wichtige Rolle spielt.
- Die Verwendung von __slots__ ist am sinnvollsten, wenn viele Instanzen einer Klasse erstellt werden und Speichereffizienz wichtig ist.
"""

