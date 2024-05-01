import logging

from AssignGamesManual import assign_games_manually
from AssignGamesOpt import assign_games_by_optimization
from CreatePairing import make_pairing
from Export import export_all
from Import import import_all

logging.basicConfig(filename="logs.log",  filemode="w", level=logging.INFO, format='%(message)s')


if __name__ == '__main__':
    # Import all data (players, games, prefs, etc.) from the input Excel file
    # TODO rename to lowercase functions
    import_all('SchandomInput.xlsx')

     #Who plays who and in which round
    make_pairing()

    # Determine which games are played in each match
    assign_games_by_optimization()

    # Export all data (pairings, optimization outcome, which games to play, etc.) to the output Excel file
    export_all('SchandomOutput.xlsx')

