class Player:
    players = []
    pairingnr_to_name = {}
    pairingnumber = 0  
    def __init__(self, new_name, rating):
        self.name = new_name
        self.rating = rating
        self.playerprefs = []
        Player.players.append(self)
        self.playedgames = []

class Match:
    def __init__(self, p1, p2):
        self.p1nr = p1
        self.p2nr = p2
        self.Game = None
        
class Game:
    games = []    
    def __init__(self, new_name):
        self.name = new_name
        self.gameprefs = []
        Game.games.append(self)       

class Preference:
    preferences = []
    def __init__(self, weight, player, game):
        self.weight = weight
        self.Player = player
        self.Game = game
        Preference.preferences.append(self)
        self.Game.gameprefs.append(self)
        self.Player.playerprefs.append(self)

class Round:
    rounds = []   
    def __init__(self, nr):
        Round.rounds.append(self)
        self.round_nr = nr
        self.matches = []
        self.playedgames = []

def GetPlayer(pnr):
    for p in Player.players:
        if p.name == Player.pairingnr_to_name[pnr]:
            return p