import logging

from AssignGamesManual import assign_games_manually
from AssignGamesOpt import AssignGamesOpt
from CreatePairing import MakePairing
from Export import ExportAll
from Import import ImportAll

logging.basicConfig(filename="logs.log",  filemode="w", level=logging.INFO, format='%(message)s')


if __name__ == '__main__':
    # Import all data (players, games, prefs, etc.) from the input Excel file
    ImportAll('SchandomInput.xlsx')

    # Who plays who and in which round
    MakePairing()

    # Determine which games are played in each match
    AssignGamesOpt()

    # Export all data (pairings, optimization outcome, which games to play, etc.) to the output Excel file
    ExportAll('SchandomOutput.xlsx')
