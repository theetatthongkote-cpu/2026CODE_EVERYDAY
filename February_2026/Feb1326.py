# day 44
# Day 44 — Learning __str__ and JSON
# Fresh practice file(chat gpt generated)

import json


# -----------------------------
# Character Class with __str__
# -----------------------------
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.full_health = health
        self.inventory = {
            "healing_potion": 3,
            "full_shield": 1,
            "half_shield": 1
        }

    # __str__ lets us control how the object prints
    def __str__(self):
        return (
            f"{self.name} | HP: {self.health}/{self.full_health} | "
            f"Potions: {self.inventory['healing_potion']} | "
            f"FullShield: {self.inventory['full_shield']} | "
            f"HalfShield: {self.inventory['half_shield']}"
        )


# -----------------------------
# JSON SAVE FUNCTION
# -----------------------------
def save_game(player):
    data = {
        "name": player.name,
        "health": player.health,
        "full_health": player.full_health,
        "inventory": player.inventory
    }

    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Game saved 💾")


# -----------------------------
# JSON LOAD FUNCTION
# -----------------------------
def load_game():
    try:
        with open("save.json", "r") as f:
            data = json.load(f)

        player = Character(data["name"], data["full_health"])
        player.health = data["health"]
        player.inventory = data["inventory"]

        print("Game loaded 📂")
        return player

    except FileNotFoundError:
        print("No save file found.")
        return None


# -----------------------------
# MAIN TEST PROGRAM
# -----------------------------
print("=== Day 44 Practice ===")

choice = input("Load previous save? (y/n): ").lower()

if choice == "y":
    player = load_game()
    if player is None:
        player = Character("Hero", 120)
else:
    player = Character("Hero", 120)

print("\nYour character:")
print(player)   # This uses __str__ automatically

# Simulate taking damage
player.health -= 25
print("\nAfter taking damage:")
print(player)

# Save progress
save_game(player)

print("\nEnd of Day 44 practice ✔")
