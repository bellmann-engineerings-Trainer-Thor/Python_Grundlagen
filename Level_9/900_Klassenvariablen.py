class Enemy:
    enemyCounter = 0

    def __init__(self):
        Enemy.enemyCounter += 1
        self.objektattribut = "Ich bin kein Klassenattribut"


print("Zugriffe über die Klasse auf die Klassenvariable")
print(Enemy.enemyCounter)                   # 0

enemy1 = Enemy()

print(Enemy.enemyCounter)                   # 1

enemy2 = Enemy()

print(Enemy.enemyCounter)                   # 2

print("Zugriffe über die Objekte auf die Klassenvariable")
print("enemy1 sagt:",enemy1.enemyCounter)   # enemy1 sagt: 2
print("enemy2 sagt:",enemy2.enemyCounter)   # enemy2 sagt: 2

print("Versuch des Zugriffs über die Klasse auf das ObjektAttribut")
print(Enemy.objektattribut)                 # AttributeError: type object 'Enemy' has no attribute 'objektattribut'
