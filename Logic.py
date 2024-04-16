from Objects import *
from Import import *
from Export import *
from CreatePairing import *
from AssignGamesManual import *
from AssignGamesOpt import *

import logging
logging.basicConfig(filename="logs.log",  filemode="w", level=logging.INFO, format='%(message)s')

#Import all data (players, games, prefs, etc.) from the input Excel file
ImportAll('SchandomInput.xlsx')

#Who plays who and in which round
MakePairing()

#Determine which games are played in each match
AssignGamesOpt()

#Export all data (pairings, optimization outcome, which games to play, etc.) to the output Excel file
ExportAll('SchandomOutput.xlsx')