from Objects import *

def AssignGames():
    weighttotal = 0
    weightlow = 1000
    weightstotal = 0
    weightslow = 1000
    for r in Round.rounds:
        for m in r.matches:
            p1 = GetPlayer(m.p1nr)
            p2 = GetPlayer(m.p2nr)
            m.prefs = {}
            if p1.name == "BYE" or p2.name == "BYE":
                continue

            for g in Game.games:
                if g in r.playedgames or g in p1.playedgames or g in p2.playedgames:
                    continue
                #include that if game is taken in round or match, then continue.
                m.prefs[g]=sum(p.weight for p in p1.playerprefs if p.Game == g) * sum(p.weight for p in p2.playerprefs if p.Game == g)

            selected_game = max(m.prefs, key=m.prefs.get)
            m.Game = selected_game
            r.playedgames.append(selected_game)
            p1.playedgames.append(selected_game)
            p2.playedgames.append(selected_game)

            #Print Stats
            p1weight = sum(p.weight for p in p1.playerprefs if p.Game == selected_game)
            p2weight = sum(p.weight for p in p2.playerprefs if p.Game == selected_game)
            if p1weight < weightlow:
                weightlow = p1weight
            if p2weight < weightlow:
                weightlow = p2weight
            if p1weight * p2weight < weightslow:
                weightslow = p1weight * p2weight
            weighttotal += p1weight + p2weight
            weightstotal += p1weight * p2weight
    
    print( weightlow, weightslow, weighttotal / 55 / 2, weightstotal / 55, weightstotal)
    