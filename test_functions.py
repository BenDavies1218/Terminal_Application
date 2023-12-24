import math

from functions import banker_offer, game_finish

# Checks the function calculates the right offer
def test_offer(): #              values left          cases left       Expected offer
    assert int(banker_offer({1: 100, 2: 100, 3: 100}, [1, 2], 3)) == 100
    assert int(banker_offer({1: 1, 2: 200, 3: 500}, [1, 2], 3)) == 310
    assert int(banker_offer({1: 150, 2: 1500, 3: 1100}, [1, 2], 3)) == 1077


# Checks game finish function works
def test_remove_case():
    assert game_finish("yes") == True
    assert game_finish("no") == False