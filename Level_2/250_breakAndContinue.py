

print("break beendet die Schleife")
for i in range(5):
    if i == 3:
        break
    print(f"i = {i}")

print("continue startet eine neue Iteration der Schleife")
for i in range(5):
    if i == 3:
        continue

print("das gilt für alle schleifen, auch der while-Schleife")

print("break verschachteln")
print("break beendet die Schleife in der es sich befindet")
for i in range(5):          # äußere Schleife i
    for j in range(5):      # innere Schleife j
        if j == 3:          # innere Schleife j
            break           # innere Schleife j
        print(f"j = {j}")   # innere Schleife j
    print(f"i = {i}")       # äußere Schleife i

print("continue verschachteln")
print("continue startet die nächste Iteration der Schleife in der es sich befindet")
for i in range(5):          # äußere Schleife i
    for j in range(5):      # innere Schleife j
        if j == 3:          # innere Schleife j
            continue        # innere Schleife j
        print(f"j = {j}")   # innere Schleife j
    print(f"i = {i}")       # äußere Schleife i