import random
import csv

file = "gamelog.csv"

def game_menu():
    print("Welcome to Deal or No Deal Will you be a millionaire \n press any button to start")
    game_start = input()

def shuffler(cases):
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow([shuffle_cases, "True"])
    return shuffle_cases

def select_case(cases_left):
    pass
    # print cases left to user
    # user will input a number between and including 1-22
    # will remove 

def game():
    pass

def banker_offer():
    pass

def game_finish():
    pass

def double_or_nothing():
    pass
