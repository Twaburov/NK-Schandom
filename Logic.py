from Objects import *
from Import import *
from Export import *
from CreatePairing import *
from AssignGames import *

import logging
logging.basicConfig(filename="logs.log",  filemode="w", level=logging.INFO, format='%(message)s')

ImportAll('SchandomInput.xlsx')
MakePairing()
AssignGames()
ExportAll('SchandomOutput.xlsx')
    
