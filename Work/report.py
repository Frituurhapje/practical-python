# report.py
#
# Exercise 2.4

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(selfself, dx, dy):
        self.x += dx
        self.y += dy

    def damage(selfself, pts):
        self.health -= pts

a = Player(2,3)
b = Player(10, 20)

print(a.x)