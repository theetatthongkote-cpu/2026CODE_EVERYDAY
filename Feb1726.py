# day 48
# chill day, no new concepts, just practice with the __str__ method and __repr__ method by myself

class Player:
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

    def __str__(self):
        return f"|{self.name}| |{self.age}| |{self.team}|"

    def __repr__(self):
        return f"Player(name='{self.name}', age={self.age}, team='{self.team}')"


Tigger = Player("Tigger", 5, "Winnie the Pooh")
Batman = Player("Batman", 35, "Gotham City")
Piglet = Player("Piglet", 3, "Winnie the Pooh")
Robin = Player("Robin", 30, "Gotham City")
# print(Tigger)
# print(repr(Batman))

players = [Tigger, Batman, Piglet, Robin]
print("(===Player Stats===):")

for p in players:
    print(p)

print("\n(===Player Repr===):")
for p in players:
    print(type(eval(repr(p))))
