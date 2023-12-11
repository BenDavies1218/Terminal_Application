import random

def shuffler(cases):
    
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    return shuffle_cases

def game():
    pass

def banker_offer():
    pass

def game_finish():
    pass

def double_or_nothing():
    pass
