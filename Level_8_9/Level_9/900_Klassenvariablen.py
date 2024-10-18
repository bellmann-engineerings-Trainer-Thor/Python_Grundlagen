class Enemy:
    staticAttribut = "ich gehöhre der Klasse"

    def __init__(self):
        self.objektAttribut = "ich bin ein ObjektAttribut"


enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
enemy4 = Enemy()

# print(Enemy.staticAttribut)
# print(enemy1.staticAttribut)

print(Enemy.objektAttribut)     # type object 'Enemy' has no attribute 'objektAttribut'
print(enemy1.staticAttribut)
print(enemy2.staticAttribut)
print(enemy3.staticAttribut)
print(enemy4.staticAttribut)
