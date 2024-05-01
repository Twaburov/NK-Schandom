from Objects import *
import logging
import random

players = Player.players

def make_pairing():
    assign_pairing_numbers()
    create_pairing_dict()
    

def assign_pairing_numbers():
    num_players = len(players)
    random.seed(0)
    pairing_numbers = random.sample(range(1, num_players+1), num_players)
    i = 0
    for player in players:
        player.pairingnumber = pairing_numbers[i]
        logging.info("Assigning pairing number " + str(player.pairingnumber) + " to player " + player.name)
        i += 1


def create_pairing_dict(): 
    for player in players:
        Player.player_dict[player.pairingnumber] = player
