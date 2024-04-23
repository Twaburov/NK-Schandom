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


def GetPlayerByPairingNumber(pnr):
    for p in Player.players:
        if p.name == Player.pairingnr_to_name[pnr]:
            return p


def GetPlayerByName(pname):
    for p in Player.players:
        if p.name == pname:
            return p


def GetPlayerWeightForGame(player, game):
    for pref in player.playerprefs:
        if pref.Game == game:
            return pref.weight


def GetAllPlayers(includeBye=True):
    all_players = Player.players.copy()
    if not includeBye:
        for p in all_players:
            if p.name == "BYE":
                all_players.remove(p)
    return all_players


class Match:
    def __init__(self, p1, p2):
        self.p1nr = p1
        self.p2nr = p2
        self.Game = None


def GetAllMatches(includeBye=True):
    matches = []
    for r in Round.rounds:
        round_matches = GetMatches(r, includeBye)
        for rm in round_matches:
            matches.append(rm)
    return matches


def GetPlayer1(match):
    return GetPlayerByPairingNumber(match.p1nr)


def GetPlayer2(match):
    return GetPlayerByPairingNumber(match.p2nr)


class Game:
    games = []

    def __init__(self, new_name):
        self.name = new_name
        self.gameprefs = []
        Game.games.append(self)


def GetGameByName(gname):
    for g in Game.games:
        if g.name == gname:
            return g


class Preference:
    preferences = []

    def __init__(self, weight, player, game):
        self.weight = weight
        self.Player = player
        self.Game = game
        Preference.preferences.append(self)
        self.Game.gameprefs.append(self)
        self.Player.playerprefs.append(self)


def GetCombinedPreference(nr1, nr2):
    return nr1 * nr2


class Round:
    rounds = []

    def __init__(self, nr):
        Round.rounds.append(self)
        self.round_nr = nr
        self.matches = []
        self.playedgames = []


def GetMatches(round, includeBye):
    matches = round.matches.copy()
    if not includeBye:
        for m in matches:
            if GetPlayer1(m).name == "BYE" or GetPlayer2(m).name == "BYE":
                matches.remove(m)
    return matches
