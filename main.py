from functions import shuffler, game, banker_offer, game_finish, double_or_nothing

cases = {
        1: 1,
        2: 5,
        3: 10,
        4: 25,
        5: 50,
        6: 75,
        7: 100,
        8: 200,
        9: 500,
        10: 750,
        11: 1000,
        12: 2500,
        13: 5000,
        14: 7500,
        15: 10000,
        16: 15000,
        17: 20000,
        18: 25000,
        19: 50000,
        20: 100000,
        21: 150000,
        22: 200000
    }


shuffled_cases = shuffler(cases)
print(shuffled_cases)
