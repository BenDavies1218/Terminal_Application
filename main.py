from colored import fg, attr, bg
from functions import game_menu, shuffler, select_case, game, banker_offer, game_finish, double_or_nothing
import csv

file = "gamelog.csv"

try:
    gamelog = open(file, "r")
    gamelog.close()

except FileNotFoundError:
    gamelog = open(file, "w")
    gamelog.write("Deal or No Deal\n")
    gamelog.close()

game_menu()

# Global variables
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
cases_left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
shuffled_cases = shuffler(cases)
user_case, cases_left = select_case(cases_left)
end_game = game_finish(cases_left)



while end_game == False:
    pass
    # interation = 0
    # count = 6 - interation
    # call game function
    # call the banker offer function
    # interation += 1

double_or_nothing()
    # includes normal end to game print cases value