from Objects import Round, Game, Player, get_player_by_pairing_number, get_combined_preference, get_player_weight_for_game

# This method can be used to create a manual pairing (in case the optimization doesn't work)


def assign_games_manually():
    for round in Round.rounds:
        for match in round.matches:
            p1 = Player.player_dict[match.p1nr]
            p2 = Player.player_dict[match.p2nr]
            match.prefs = {}
            if "BYE" in (p1.name, p2.name):
                continue

            # If the game is already played by either player or by another match in the same round, it won't be an
            # option for the match
            for game in Game.games:
                if game in round.playedgames or game in p1.playedgames or game in p2.playedgames:
                    continue
                match.prefs[game] = get_combined_preference(get_player_weight_for_game(p1, game),
                                                          get_player_weight_for_game(p2, game))

            # Just pick the game with the highest combined pref for this round
            selected_game = max(match.prefs, key=match.prefs.get)
            match.Game = selected_game
            round.playedgames.append(selected_game)
            p1.playedgames.append(selected_game)
            p2.playedgames.append(selected_game)
