from Objects import *

def ImportAll(filename):
    import openpyxl 
    wb = openpyxl.load_workbook(filename)

    ImportPlayers(wb['Players'])
    ImportGames(wb['Games'])
    ImportPrefences(wb['Prefs'])
    
def ImportPlayers(ws_players):
    for i in range(2,ws_players.max_row+1):
        Player(ws_players.cell(row=i,column=1).value, ws_players.cell(row=i,column=2).value)

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

