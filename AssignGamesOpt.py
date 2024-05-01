from Objects import get_all_matches, Game, get_combined_preference, get_player_weight_for_game, get_player1, get_all_players, \
    Round, get_matches, get_player2
from pyomo.environ import Objective, Var, ConstraintList, Binary
from pyomo.core import maximize, ConcreteModel
from pyomo.opt import SolverFactory



def assign_games_by_optimization():
    model = ConcreteModel()
    combinedprefs = {}
    all_matches = get_all_matches(False)
    all_games = Game.games
    all_players = get_all_players(False)
    all_rounds = Round.rounds

    # Variables
    model.x = Var(all_matches, all_games, domain=Binary)

    # Objective Function
    model.obj = Objective(expr=sum(model.x[m, g] * get_combined_preference(get_player_weight_for_game(get_player1(m), g),
                                                                         get_player_weight_for_game(get_player2(m), g))
                                   for m in all_matches for g in all_games), sense=maximize)

    # Constraints
    # For each match you have to select exactly one game.
    model.game_one_per_match = ConstraintList()
    for match in all_matches:
        model.game_one_per_match.add(sum(model.x[match, g] for g in all_games) == 1.0)

    # In each round only one match can play a particular game.
    model.game_once_per_round = ConstraintList()
    for round in all_rounds:
        for game in all_games:
            model.game_once_per_round.add(sum(model.x[m, game] for m in get_matches(round, False)) <= 1.0)

    # Each player can play every game only once in the whole tournament.
    model.game_once_per_player = ConstraintList()
    for player in all_players:
        for game in all_games:
            model.game_once_per_player.add(
                sum(model.x[m, game] for m in all_matches if (get_player1(m) == player or get_player2(m) == player)) <= 1.0)

    # solve
    results = SolverFactory('glpk').solve(model)
    results.write()
    if results.solver.status:
        pass  # Can print the model:
        # model.pprint()

    # Handle Result
    for match in all_matches:
        for game in all_games:
            if model.x[match, game].value == 1.0:
                match.Game = game  # This sets the solution
                # Print the output in console, later will be written to Excel in Export.py
                print(get_player1(match).name, get_player2(match).name, game.name)
