# day 39
# inventory system

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
        self.inventory = {
            "healing_potion": 3,
            "sword": 5,
            "full_shield": 2,
            "half_shield": 2

        }
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
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(
            f"{self.name} took {amount} damage. Health: {self.health}/{self.full_health}")

    def heal(self, amount=None):
        if amount is None:
            amount = random.randint(15, 30)
        self.health += amount
        if self.health > self.full_health:
            self.health = self.full_health
        self.heal_cooldown = 3
        print(
            f"{self.name} used a healing potion to gain {amount} HP. Total Health: {self.health}")
        if self.heal_cooldown > 0:
            print(f"{self.name} can't heal for {self.heal_cooldown} more turn(s)!")
            return

    def full_block(self):
        self.is_full_blocking = True
        self.is_half_blocking = False
        self.full_block_cooldown = 2
        print(f"{self.name} is blocking the next attack completely!")
        if self.full_block_cooldown > 0:
            print(
                f"{self.name} can't full block for {self.full_block_cooldown} more turn(s)!")
        return

    def half_block(self):
        self.is_half_blocking = True
        self.is_full_blocking = False
        self.half_block_cooldown = 2
        print(f"{self.name} is blocking half of the next attack!")
        if self.half_block_cooldown > 0:
            print(
                f"{self.name} can't half block for {self.half_block_cooldown} more turn(s)!")
        return

    @staticmethod
    def enemy_attack(enemy, player):
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

    @staticmethod
    def player_turn(player, enemy):
        print("\nYour turn!")
        print("|<---1 = Attack | 2 = Full Block | 3 = Half Block | 4 = Heal| 5 = Show Inventory--->|")

        choice = input("> ")

        if choice == "1":
            enemy.take_damage()
        elif choice == "2":
            player.full_block()
        elif choice == "3":
            player.half_block()
        elif choice == "4":
            player.heal()
        elif choice == "5":
            player.show_inventory()
            item_choice = input(
                "Use which item? (Use which item? (healing_potion/full_shield/half_shield/sword)): ").lower()

            if item_choice != "":
                player.use_item(item_choice, enemy)

    def reduce_cooldowns(self):
        if self.heal_cooldown > 0:
            self.heal_cooldown -= 1
        if self.full_block_cooldown > 0:
            self.full_block_cooldown -= 1
        if self.half_block_cooldown > 0:
            self.half_block_cooldown -= 1

    def show_inventory(self):
        print(f"<---{self.name}'s Inventory--->")
        for item, qty in self.inventory.items():
            print(f"<---{item}: {qty}--->")

    def use_item(self, item, enemy=None):
        if item not in self.inventory:
            print(f"{item} not found in inventory.")
            return
        if self.inventory[item] <= 0:
            print(f"No {item} left to use.")
            return
        if item == "healing_potion":
            self.heal()
            self.inventory[item] -= 1
            print(f"Used {item}! Remaining: {self.inventory[item]}")
        elif item == "sword":
            damage = random.randint(18, 30)
            print(f"{self.name} strikes with the sword for {damage} damage!")
            self.inventory[item] -= 1
            if enemy:
                enemy.take_damage(damage)
            print(f"Used {item}! Remaining: {self.inventory[item]}")
            return damage
        elif item == "full_shield":
            self.full_block()
            self.inventory[item] -= 1
            print(f"Used {item}! Remaining: {self.inventory[item]}")
        elif item == "half_shield":
            self.half_block()
            self.inventory[item] -= 1
            print(f"Used {item}! Remaining: {self.inventory[item]}")
        else:
            print(f"{item} cannot be used.")

        # ---------- GAME LOOP ----------
player = Character("Goblindestroyer123", health=120)
enemy = Character("Big Goblin", health=60)
turn = 1
while player.health > 0 and enemy.health > 0:
    print(f"\n===== TURN {turn} =====")
    Character.player_turn(player, enemy)
    player.show_inventory()
    player.reduce_cooldowns()
    enemy.reduce_cooldowns()
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

again = input("\nPlay again? (y/n): ").lower()
if again != "y":
    print("Thanks for playing 😄")
