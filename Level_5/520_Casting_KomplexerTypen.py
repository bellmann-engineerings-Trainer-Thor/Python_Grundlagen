## Von String zu Collections

# String zu Liste
x = "1,2,3"
liste_von_string = x.split(',')
print(liste_von_string)  # Ausgabe: ['1', '2', '3']

# String zu Tuple
tuple_von_string = tuple(x.split(','))
print(tuple_von_string)  # Ausgabe: ('1', '2', '3')

# String zu Set
set_von_string = set(x.split(','))
print(set_von_string)  # Ausgabe: {'1', '2', '3'}

## Von Collections zu Collections

# Liste zu Tuple
liste = [1, 2, 3]
tuple_von_liste = tuple(liste)
print(tuple_von_liste)  # Ausgabe: (1, 2, 3)

# Liste zu Set
set_von_liste = set(liste)
print(set_von_liste)  # Ausgabe: {1, 2, 3}

# Tuple zu Liste
tupel = (4, 5, 6)
liste_von_tuple = list(tupel)
print(liste_von_tuple)  # Ausgabe: [4, 5, 6]

# Tuple zu Set
set_von_tuple = set(tupel)
print(set_von_tuple)  # Ausgabe: {4, 5, 6}

# Set zu Liste
set1 = {7, 8, 9}
liste_von_set = list(set1)
print(liste_von_set)  # Ausgabe: [7, 8, 9] (Reihenfolge kann variieren)

# Set zu Tuple
tuple_von_set = tuple(set1)
print(tuple_von_set)  # Ausgabe: (7, 8, 9) (Reihenfolge kann variieren)
