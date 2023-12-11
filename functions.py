import random

def game_menu():
    print("Welcome to Deal or No Deal Will you be a millionaire \n press any button to start")
    game_start = input()

def shuffler(cases):
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    return shuffle_cases

def select_case(cases):
    pass

def game():
    pass

def banker_offer():
    pass

def game_finish():
    pass

def double_or_nothing():
    pass
