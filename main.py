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
cases_left = ["|", "1", "|", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

game_menu()
shuffled_cases = shuffler(cases)
select_case(cases_left)
