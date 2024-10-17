# Karten mischen
#
# Schreibe ein Programm, das das Mischen der 32 Karten eines Skatspiels simuliert.
# Jede Karte wird durch eine Liste der Form [Farbe, Wert] dargestellt.
# Die Farben sind: Kreuz, Pik, Herz und Karo.
# Die Werte sind: Ass, König, Dame, Bube, Zehn, Neun, Acht, Sieben.
#
# Zunächst wird eine Liste mit den 32 Karten-Listen erstellt.
#
# Durch wiederholtes Vertauschen zweier zufällig ausgewählter
# Karten sollen die Listen dann noch gemischt werden.
#
# Die Ausgabe könnte folgendermaßen aussehen:
#
# Ungemischt:
# [Kreuz, Sieben] [Kreuz, Acht]   [Kreuz, Neun]   [Kreuz, Zehn]   [Kreuz, Bube]   [Kreuz, Dame]   [Kreuz, König]  [Kreuz, Ass]
# [Pik, Sieben]   [Pik, Acht]     [Pik, Neun]     [Pik, Zehn]     [Pik, Bube]     [Pik, Dame]     [Pik, König]    [Pik, Ass]
# [Herz, Sieben]  [Herz, Acht]    [Herz, Neun]    [Herz, Zehn]    [Herz, Bube]    [Herz, Dame]    [Herz, König]   [Herz, Ass]
# [Karo, Sieben]  [Karo, Acht]    [Karo, Neun]    [Karo, Zehn]    [Karo, Bube]    [Karo, Dame]    [Karo, König]   [Karo, Ass]
#
# Gemischt:
# [Karo, Dame]    [Herz, König]   [Pik, Neun]     [Pik, Ass]      [Herz, Ass]     [Kreuz, Zehn]   [Karo, Sieben]  [Kreuz, Bube]
# [Pik, Zehn]     [Kreuz, Neun]   [Pik, Acht]     [Karo, König]   [Pik, Sieben]   [Herz, Bube]    [Kreuz, Dame]   [Karo, Neun]
# [Pik, Bube]     [Karo, Acht]    [Herz, Zehn]    [Kreuz, Acht]   [Kreuz, König]  [Kreuz, Sieben] [Pik, Dame]     [Kreuz, Ass]
# [Pik, König]    [Herz, Sieben]  [Herz, Neun]    [Herz, Acht]    [Herz, Dame]    [Karo, Zehn]    [Karo, Bube]    [Karo, Ass]
