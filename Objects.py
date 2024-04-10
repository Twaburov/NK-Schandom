class Player:
    players = []
    pairingnumber = 0
    def __init__(self, new_name, rating):
        self.name = new_name
        self.rating = rating
        self.individualprefs = []
        Player.players.append(self)

class Game:
    games = []
    def __init__(self, new_name):
        self.name = new_name
        Game.games.append(self)

class Preference:
    preferences = []
    def __init__(self, weight, player, game):
        self.weight = weight
        self.Player = player
        self.Game = game
        Preference.preferences.append(self)
        self.Player.individualprefs.append(self)

class Round:
    def __init__(self, nr):
        self.round_number = nr
        self.matches = []