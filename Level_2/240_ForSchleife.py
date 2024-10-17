print("for-schleife")
for i in range(5):
    print(i)


i = 0
while i < 5:
    print(i)
    i += 1
#
print("range mit 2 Argumenten")
start = 5
stop = 10
for i in range(start, stop):
    print(i)
#
print("range mit 3 Argumenten")
start = 2
stop = 10
step = 2
for i in range(start, stop, step):
    print(i)
# #
# # print("normale benutzung der benutzerdefinierten for-Schleife")
for i in range(1, 15, 4):
    print(i)
# #
# # print("Beispiel2: Benutzerdefinierte for-Schleife")
# # startpunkt = 50
# # endpunkt = 0
# # schrittweite = -10
# # for i in range(startpunkt, endpunkt, schrittweite):
# #     print(i)
# #
# #
# #
# # print("Beispiel3: Benutzerdefinierte for-Schleife")
# # for i in range(6, -1, -2):
# #     print(i)