# day 38
# Cooldowns + Time System + Crits
import random
import time


class Character:
    total_charaters = 0

    def __init__(self, name, health=110):
        self.name = name
        self.health = health
        self.full_health = health
        self.is_full_blocking = False
        self.is_half_blocking = False
        self.heal_cooldown = 0
        self.full_block_cooldown = 0
        self.half_block_cooldown = 0
        Character.total_charaters += 1

    def take_damage(self, amount=None):
        if amount is None:
            amount = random.randint(5, 16)
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
        elif self.health < 0:
            print(f"{self.name} is already defeated and cannot take more damage.")
            return

        self.health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.health}")

    def heal(self, amount=None):
        if amount is None:
            amount = random.randint(15, 30)
        self.health += amount

        if self.health > self.full_health:
            self.health = self.full_health
        self.heal_cooldown = 3
        print(
            f"{self.name} used a healing potion to gain {amount} HP. Total Health: {self.health}")

    def full_block(self):
        self.is_full_blocking = True
        self.is_half_blocking = False
        self.full_block_cooldown = 2
        print(f"{self.name} is blocking the next attack completely!")

    def half_block(self):
        self.is_half_blocking = True
        self.is_full_blocking = False
        self.half_block_cooldown = 2
        print(f"{self.name} is blocking half of the next attack!")

    @classmethod
    def enemy_attack(self, enemy, player):
        action = random.choice(["full_block", "half_block", "attack", "heal"])
        if enemy.health < enemy.full_health * 0.4:
            action = random.choice(["heal", "attack", "full_block"])
        else:
            action = random.choice(["attack", "full_block", "half_block"])
        if action == "full_block":
            enemy.full_block()
            print(f"{enemy.name} is preparing to block fully!")
        elif action == "half_block":
            enemy.half_block()
            print(f"{enemy.name} is preparing to block half!")
        elif action == "attack":
            damage = random.randint(5, 16)
            print(f"{enemy.name} attacks {player.name} for {damage} damage!")
            player.take_damage(damage)
        elif action == "heal":
            heal_amount = random.randint(15, 30)
            enemy.heal(heal_amount)

    @classmethod
    def player_turn(self, player, enemy):
        print("\nYour turn!")
        print("1 = Attack | 2 = Full Block | 3 = Half Block | 4 = Heal")

        choice = input("> ")

        if choice == "1":
            enemy.take_damage()
        elif choice == "2":
            player.full_block()
        elif choice == "3":
            player.half_block()

        elif choice == "4":
            player.heal()

    def reduce_cooldowns(self):
        if self.heal_cooldown > 0:
            self.heal_cooldown -= 1
        if self.full_block_cooldown > 0:
            self.full_block_cooldown -= 1
        if self.half_block_cooldown > 0:
            self.half_block_cooldown -= 1


# ---------- GAME LOOP ----------
player = Character("Goblindestroyer123", health=120)
enemy = Character("Big Goblin", health=60)
turn = 1
while player.health > 0 and enemy.health > 0:
    Character.player_turn(player, enemy)
    print(f"\n===== TURN {turn} =====")
    turn += 1
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated!")
        break
    time.sleep(1)
    Character.enemy_attack(enemy, player)
    if player.health <= 0:
        print(f"{player.name} has been defeated!")
        break
    time.sleep(1)
