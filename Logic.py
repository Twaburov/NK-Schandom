from Objects import *
from Import import *

ImportAll('Schandom.xlsx')

#Print the read-in data
print(len(Player.players), len(Game.games), len(Preference.preferences))
'''
for p in Player.players:
    print(p.name, p.rating)
for g in Game.games:
    print(g.name)
for pr in Preference.preferences:
    print(pr.Weight, pr.Player, pr.Game)
'''

for pref in Preference.preferences:
    print(pref.weight, pref.Player.name, pref.Game.name)

for playa in Player.players:
    print(len(playa.individualprefs))