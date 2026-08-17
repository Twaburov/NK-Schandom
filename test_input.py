from Objects import *
from Import import import_all
import pytest


@pytest.fixture
def process_input(scope="session"):
    import_all('TestInput.xlsx')


# TODO: je kan de testen eenvoudig uitbreiden. Ik zou hiervoor gebruik maken van het TestInput.xlsx bestand,
#  dan kan je de echte input iedere keer wijzigen.
#  Je ziet nu ook dat 2x de process_input aanroepen niet helemaal goed gaat.
def test_players(process_input):
    assert len(Player.players) == 12


def test_games():
    assert len(Game.games) == 36
