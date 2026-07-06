# day 36
class Player:
    total_players = 0

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.full_health = health
        self.is_full_blocking = False
        self.is_half_blocking = False
        Player.total_players += 1

    def take_damage(self, amount=10):
        if self.is_full_blocking:
            print(f"{self.name} blocked the attack and took no damage!")
            amount = 0
            self.is_full_blocking = False
            print(f"{self.name}'s blocking has worn off.")
        elif self.is_half_blocking:
            blocked_amount = amount // 2
            amount -= blocked_amount
            print(
                f"{self.name} blocked half the attack, reducing damage by {blocked_amount}.")
            self.is_half_blocking = False
            print(f"{self.name}'s blocking has worn off.")

        self.health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.health}")

    def heal(self, amount=20):
        self.health += amount

        if self.health > self.full_health:
            self.health = self.full_health
        # or you can use
        # def heal(self, amount=20):
         # self.health = min(self.health + amount, self.full_health)
         # print(f"{self.name} healed {amount} HP. Health: {self.health}/{self.full_health}")
        print(
            f"{self.name} used a healing potion to gain {amount} HP. Total Health: {self.health}")

    def full_block(self):
        self.is_full_blocking = True
        self.is_half_blocking = False
        print(f"{self.name} is blocking the next attack completely!")

    def half_block(self):
        self.is_half_blocking = True
        self.is_full_blocking = False
        print(f"{self.name} is blocking half of the next attack!")

    @classmethod
    def get_player_count(cls):
        return cls.total_players


p1 = Player("Tigger")
p2 = Player("Kunkao")

# p1.take_damage()
# p1.heal()
# p2.take_damage()
# p2.heal()

# print("Total players:", Player.get_player_count())
p1.take_damage(30)
p1.block(30)
print(p1.health)
