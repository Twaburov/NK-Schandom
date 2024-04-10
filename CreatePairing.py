from Objects import *
import logging
import random

cup = []
players = Player.players

def MakePairing():
    CreatePairingNumbers()
    AssignPairingNumbers()

def CreatePairingNumbers():
    for i in range(len(players)):
        cup.append(i+1)

def AssignPairingNumbers():
    logging.info("Assigning Pairing Numbers")
    for player in players:
        pairing_number = random.choice(cup)
        player.pairingnumber = pairing_number
        logging.info("Assining pairing number " + str(player.pairingnumber) + " to player " + player.name)
        cup.remove(pairing_number)

