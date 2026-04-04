# day 49
# @classmethod + simple object storage(JSON review combo)
import json
import os


class Player:
    player_count = 0
    players = []

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Player.player_count += 1
        Player.players.append(self)

    def __str__(self):
        return f"|{self.name}| |{self.score}|"

    def __repr__(self):
        return f"Player {self.name} | Score: {self.score}"

    @classmethod
    def load_users(cls, file_path):
        if not os.path.exists(file_path):
            return
        cls.players.clear()  # Clear existing players before loading new ones
        cls.player_count = 0  # Reset player count before loading new ones
        with open(file_path, 'r') as file:
            data = json.load(file)
            for player_data in data:
                player = Player(player_data['name'], player_data['score'])
                Player.players.append(player)

    @classmethod
    def save_users(cls, file_path):
        data = [p.to_dict() for p in cls.players]
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score
        }


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
