from Objects import *

#This method can be used to create a manual pairing (in case the optimization doesn't work)
def AssignGamesManual():
    weighttotal = 0
    weightlow = 1000
    weightstotal = 0
    weightslow = 1000
    for r in Round.rounds:       
        for m in r.matches:
            p1 = GetPlayerByPairingNumber(m.p1nr)
            p2 = GetPlayerByPairingNumber(m.p2nr)
            m.prefs = {}
            if p1.name == "BYE" or p2.name == "BYE":
                continue

            for g in Game.games:
                #If the game is already played by either player or by another match in the same round, it won't be an option for the match
                if g in r.playedgames or g in p1.playedgames or g in p2.playedgames:
                    continue
                m.prefs[g]= GetCombinedPreference(GetPlayerWeightForGame(p1,g), GetPlayerWeightForGame(p2,g))

            selected_game = max(m.prefs, key=m.prefs.get) #Just pick the game with the highest combined pref for thsi round
            m.Game = selected_game
            r.playedgames.append(selected_game)
            p1.playedgames.append(selected_game)
            p2.playedgames.append(selected_game)
    