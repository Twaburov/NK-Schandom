from Objects import *
import logging
import random

cup = []
players = Player.players

def MakePairing():
    CreatePairingNumbers()
    AssignPairingNumbers()
    CreatePairingDict()

def CreatePairingNumbers():
    for i in range(len(players)):
        cup.append(i+1)

def AssignPairingNumbers():
    logging.info("Assigning Pairing Numbers")

    random.seed(0)
    for player in players:
        pairing_number = random.choice(cup)
        player.pairingnumber = pairing_number
        logging.info("Assigning pairing number " + str(player.pairingnumber) + " to player " + player.name)
        cup.remove(pairing_number)

def CreatePairingDict():
    for p in players:
        Player.pairingnr_to_name[p.pairingnumber]= p.name
    Player.pairingnr_to_name = dict(sorted(Player.pairingnr_to_name.items()))

