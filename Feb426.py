# day 35
class Player:
    total_players = 0

    def __init__(self, name):
        self.name = name
        self.health = 100
        Player.total_players += 1

    def take_damage(self, amount=10):
        self.health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.health}")

    def heal(self, amount=20):
        self.health += amount
        print(
            f"{self.name} used a healing potion to gain {amount} HP. Total Health: {self.health}")

    @classmethod
    def get_player_count(cls):
        return cls.total_players


p1 = Player("Tigger")
p2 = Player("Tiger")

p1.take_damage()
p1.heal()
p2.take_damage()
p2.heal()

print("Total players:", Player.get_player_count())
