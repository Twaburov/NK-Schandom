class Player:
    players = []
    player_dict = {}
    pairingnumber = 0

    def __init__(self, new_name, rating):
        self.name = new_name
        self.rating = rating
        self.playerprefs = []
        self.playedgames = []
        Player.player_dict[new_name] = self
        Player.players.append(self)
        

def get_player_by_pairing_number(pnr):
    for player in Player.players:
        if player == Player.player_dict[pnr]:
            return player


def get_player_by_name(pname):
    for player in Player.players:
        if player == Player.player_dict[pname]:
            return player


def get_player_weight_for_game(player, game):
    for pref in player.playerprefs:
        if pref.Game == game:
            return pref.weight


def get_all_players(includeBye=True):
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


def get_all_matches(includeBye=True):
    matches = []
    for r in Round.rounds:
        round_matches = get_matches(r, includeBye)
        for rm in round_matches:
            matches.append(rm)
    return matches


def get_player1(match):
    return get_player_by_pairing_number(match.p1nr)


def get_player2(match):
    return get_player_by_pairing_number(match.p2nr)


class Game:
    games = []

    def __init__(self, new_name):
        self.name = new_name
        self.gameprefs = []
        Game.games.append(self)


def get_game_by_name(gname):
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


def get_combined_preference(nr1, nr2):
    return nr1 * nr2


class Round:
    rounds = []

    def __init__(self, nr):
        Round.rounds.append(self)
        self.round_nr = nr
        self.matches = []
        self.playedgames = []


def get_matches(round, includeBye):
    matches = round.matches.copy()
    if not includeBye:
        for m in matches:
            if get_player1(m).name == "BYE" or get_player2(m).name == "BYE":
                matches.remove(m)
    return matches
