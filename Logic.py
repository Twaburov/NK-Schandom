from Objects import *
from Import import *
from CreatePairing import *

import logging
logging.basicConfig(filename="logs.log",  filemode="w", level=logging.INFO, format='%(message)s')

ImportAll('Schandom.xlsx')
MakePairing()
    
