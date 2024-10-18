# Roboter
#
# Wir haben folgende einfache Roboterklasse geschrieben:
#
# class Roboter:
#     def __init__(self, name):
#         self.name = name
#
# Diese Klasse erfreut sich nun auf einmal weltweit großer Beliebtheit.
# Wir haben allerdings ein Problem:
# Die internationale Robotergewerkschaft konnte ein weltweites Verbot durchsetzen,
# dass Roboter nicht mehr "Bernd" genannt werden dürfen.
# Schreibe nun die Klasse so um,
# dass Roboter automatisch "Herbert" genannt werden,
# wenn jemand versucht, sie "Bernd" zu taufen
# oder versucht den Roboter in "Bernd" umzubenennen.
#
# Für die Benutzer der Klasse darf sich natürlich nichts ändern.
# Nur muss jetzt zweimal "Herbert" ausgegeben werden.
#
# Bitte auch das Umbenennen testen.
# Nach dem Versuch, einen Roboter in „Bernd” umzubenennen,
# muss dieser Roboter „Herbert” heißen:
#
#

class Roboter:
    def __init__(self, name):
        self.name = name


a = Roboter("Bernd")
print(a.name)  # Herbert

b = Roboter("Stefan")
b.name = "Bernd"
print(b.name)  # Herbert

c = Roboter("Peter")
print(c.name)  # Peter