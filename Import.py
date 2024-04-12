from Objects import *
nr_of_players = 0

def ImportAll(filename):
    import openpyxl 
    wb = openpyxl.load_workbook(filename)

    ImportPlayers(wb['Players'])
    ImportGames(wb['Games'])
    ImportPrefences(wb['Prefs'])
    ImportBerger(wb["Berger" + str(len(Player.players))])
    
def ImportPlayers(ws_players):
    for i in range(2,ws_players.max_row+1):
        Player(ws_players.cell(row=i,column=1).value, ws_players.cell(row=i,column=2).value)
    global nr_of_players
    nr_of_players = len(Player.players)

def ImportGames(ws_games):
    for i in range(2,ws_games.max_row+1):
        Game(ws_games.cell(row=i,column=1).value)

def ImportPrefences(ws_preferences):
    for i in range(2,ws_preferences.max_column+1):
        for player in Player.players:
            if player.name == ws_preferences.cell(row=1,column=i).value:
                for j in range(2,ws_preferences.max_row+1):
                    for game in Game.games:
                        if game.name == ws_preferences.cell(row=j,column=1).value:
                            Preference(ws_preferences.cell(row=j,column=i).value,
                            player,
                            game)
                            continue
                continue

def ImportBerger(ws_berger):
    for i in range(1,nr_of_players):
        round_i = Round(i)
        for j in range(1,int(nr_of_players/2)):
            pairing_nrs = ws_berger.cell(row=i,column=j).value.split(':')           
            round_i.matches.append(Match(int(pairing_nrs[0]),int(pairing_nrs[1])))
