""" Code for calculating a player's chance of winning a game based
on their elo and that of their opponent.
In addition, calculates their new elo given the outcome of the match
versus the expected result. """

def win_chance(a, b):
    """ Returns the chances of player a winning the game. """
    exponent = (b - a) / 400
    return 1 / (1 + 10**exponent)

def calculate_new_rating(rating, score, expected_score):
    """ Returns the new rating of a player, given their rating,
    as well as the score and expected_score of a game. """
    return rating + 32 * (score - expected_score)

if __name__ == "__main__":
    # Testing code
    a = 1656
    b = 1763
    chance = win_chance(a, b)
    new_rating = calculate_new_rating(a, 1, chance)
    print(new_rating)

    