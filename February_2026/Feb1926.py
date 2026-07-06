# day 50
# analysing yesterday's code and adding some error handling to the file operations
from fileinput import filename
import json
import os
# Creates player objects
# Tracks total players (player_count)
# Stores players in a class list (players)
# Saves players → JSON file
# Loads players ← JSON file
# Prints them nicely


class Player:
    player_count = 0  # player_count tracks how many Player objects were created
    players = []  # players stores every player object created in a list

    # Creates a player Saves name + score, Increases total player count
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Player.player_count += 1
        Player.players.append(self)

    def __str__(self):  # pretty print for users
        return f"|{self.name}| |{self.score}|"

    def __repr__(self):  # debug / developer view
        return f"Player(name='{self.name}', score={self.score})"

    @classmethod
    def load_users(cls, file_path):
        if not os.path.exists(file_path):  # Prevents crash if file missing.
            return
        cls.players.clear()  # Clear existing players before loading new ones
        cls.player_count = 0  # Reset player count before loading new ones
        with open(file_path, 'r') as file:
            data = json.load(file)  # Reads JSON → Python list of dictionaries.
            for player_data in data:
                # Rebuilds Player objects from saved data.
                player = Player(player_data['name'], player_data['score'])
                cls.players.append(player)
                cls.player_count += 1

    @classmethod
    def save_users(cls, file_path):
        data = [p.to_dict() for p in cls.players]
        with open(file_path, "w") as f:
            # Converts objects → dictionaries → JSON file
            json.dump(data, f, indent=4)  # Clean and Pythonic.

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score
        }

    def find_player(cls, name):
        for player in cls.players:
            if player.name == name:
                return player
        return None  # Return None if player not found


Tigger = Player("Tigger", 5)
Batman = Player("Batman", 35)
Piglet = Player("Piglet", 3)
Robin = Player("Robin", 30)

Player.save_users("players.json")

print("Saved Players:")
for player_data in Player.players:
    print(player_data)

print("\nReloading from JSON...\n")

Player.load_users("players.json")

for p in Player.players:
    print(p)

print("\nTotal Players:", Player.player_count)
