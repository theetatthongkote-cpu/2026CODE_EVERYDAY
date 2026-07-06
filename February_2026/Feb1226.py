# day 43
# white splash vs avatar basketball game

class White_Splash_Player:
    player_count = 0
    total_score = 0

    def __init__(self, name, points, jersey_number):
        self.name = name
        self.points = points
        self.jersey_number = jersey_number
        White_Splash_Player.player_count += 1
        White_Splash_Player.total_score += points

    @classmethod
    def get_white_splash_player_count(cls):
        return (cls.player_count)


class Avatar_Player:
    player_count = 0   # class variable
    total_score = 0

    def __init__(self, name, points, jersey_number):
        self.name = name
        self.points = points
        self.jersey_number = jersey_number
        Avatar_Player.player_count += 1
        Avatar_Player.total_score = points

    @classmethod
    def get_avatar_player_count(cls):
        return (cls.player_count)


Eto = Avatar_Player("Eto", 10, "#11")
Tigger = White_Splash_Player("Tigger", 2, "#9")
print(Avatar_Player.get_avatar_player_count())

print(White_Splash_Player.get_white_splash_player_count())

print(Tigger.jersey_number)
