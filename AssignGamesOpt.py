from Objects import *
from pyomo.environ import *

def AssignGamesOpt():
    model = ConcreteModel()
    combinedprefs = {}
    all_matches = GetAllMatches(False)
    all_games = Game.games
    all_players= GetAllPlayers(False)
    all_rounds = Round.rounds

    #Variables
    model.x = Var( all_matches, all_games, domain = Boolean)

    #Objective Function
    model.obj = Objective( expr = sum( model.x[m,g] * GetCombinedPreference( GetPlayerWeightForGame(GetPlayer1(m), g), GetPlayerWeightForGame(GetPlayer2(m), g) ) 
                                      for m in all_matches for g in all_games), sense = maximize )
    
    #Constraints
    #For each match you have to select exactly one game.
    model.game_one_per_match = ConstraintList()
    for m in all_matches:
        model.game_one_per_match.add(sum(model.x[m,g] for g in all_games) == 1.0)

    #In each round only one match can play a particular game.
    model.game_once_per_round = ConstraintList()
    for r in all_rounds:
        for g in all_games:
            model.game_once_per_round.add(sum(model.x[m,g] for m in GetMatches(r,False)) <= 1.0)
    
    #Each player can play every game only once in the whole tournament.
    model.game_once_per_player = ConstraintList()
    for p in all_players:
        for g in all_games:
            model.game_once_per_player.add(sum(model.x[m,g] for m in all_matches if (GetPlayer1(m)==p or GetPlayer2(m)==p)) <= 1.0)

    # solve
    results = SolverFactory('glpk').solve(model)
    results.write()
    if results.solver.status:
        pass #Can print the model:
        #model.pprint()

    #Handle Result
    for m in all_matches:
        for g in all_games:
            if model.x[m,g].value == 1.0:
                m.Game = g #This sets the solution
                #Print the output in console, later will be written to Excel in Export.py
                print(GetPlayer1(m).name, GetPlayer2(m).name, g.name) 
