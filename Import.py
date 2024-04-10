from Objects import *

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
    nr_of_players = len(Player.players)

def ImportGames(ws_games):
    for i in range(2,ws_games.max_row+1):
        Game(ws_games.cell(row=i,column=1).value)

def ImportPrefences(ws_preferences):
    for i in range(2,ws_preferences.max_row+1):
        for player in Player.players:
            if player.name == ws_preferences.cell(row=i,column=2).value:
                for game in Game.games:
                    if game.name == ws_preferences.cell(row=i,column=3).value:
                        Preference(ws_preferences.cell(row=i,column=1).value,
                        player,
                        game)

def ImportBerger(ws_berger):
    for i in range(1,len(Player.players)):
        ronde = Round(i)
        for j in range(1,int(len(Player.players)/2)):
            ronde.matches.append(ws_berger.cell(row=i,column=j).value.split(':'))
        print(ronde.round_number, ronde.matches)
