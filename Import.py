from Objects import *

nr_of_players = 0


def import_all(filename):
    import openpyxl
    wb = openpyxl.load_workbook(filename)

    import_players(wb['Players'])
    import_games(wb['Games'])
    import_preferences(wb)
    import_restrictions(wb['Restrictions'])
    # Import the Berger tabel to initiate a Round Robin pairing.
    import_berger(wb["Berger" + str(len(Player.players))])


def import_players(ws_players):
    for i in range(2, ws_players.max_row + 1):
        Player(ws_players.cell(row=i, column=1).value, ws_players.cell(row=i, column=2).value)
    global nr_of_players
    nr_of_players = len(Player.players)


def import_games(ws_games):
    for i in range(2, ws_games.max_row + 1):
        Game(ws_games.cell(row=i, column=1).value)


# Imports the Prefs table
def import_preferences(wb):
    for player in Player.players:
        if player.name == "BYE":
            continue
        sheet_name = "Prefs" + player.name
        if sheet_name not in wb.sheetnames:
            raise ValueError(f"Ontbrekend voorkeuren-tabblad: {sheet_name}")
        ws = wb[sheet_name]

        # kolommen -> tegenstander, gelezen uit de headerrij (op naam, niet op positie)
        opponents = {}
        for col in range(2, ws.max_column + 1):
            opp_name = ws.cell(row=1, column=col).value
            if opp_name is not None:
                opponents[col] = get_player_by_name(opp_name)

        # per spelrij een gewicht per tegenstander-kolom
        for row in range(2, ws.max_row + 1):
            game_name = ws.cell(row=row, column=1).value
            if game_name is None:
                continue
            game = get_game_by_name(game_name)
            for col, opponent in opponents.items():
                weight = ws.cell(row=row, column=col).value
                Preference(weight, player, game, opponent)

def import_restrictions(ws_restrictions):
    for row in range(2, ws_restrictions.max_row + 1):
        group_id = ws_restrictions.cell(row=row, column=1).value
        name     = ws_restrictions.cell(row=row, column=2).value
        game_nm  = ws_restrictions.cell(row=row, column=3).value
        capacity = ws_restrictions.cell(row=row, column=4).value
        if group_id is None or game_nm is None:
            continue
        game = get_game_by_name(game_nm)
        if game is None:
            raise ValueError(
                f"Restrictie verwijst naar onbekend spel '{game_nm}'. "
                f"Naam moet exact matchen met het tabblad Games.")
        restriction = get_restriction(group_id, name, capacity)
        restriction.add_game(game)
        
def import_berger(ws_berger):
    for i in range(1, nr_of_players):
        round_i = Round(i)
        for j in range(1, int(nr_of_players / 2) + 1):
            pairing_nrs = ws_berger.cell(row=i, column=j).value.split(':')
            round_i.matches.append(Match(int(pairing_nrs[0]), int(pairing_nrs[1])))
