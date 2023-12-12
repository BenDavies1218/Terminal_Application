import random
import csv

file = "gamelog.csv"

def game_menu():
    print("Welcome to Deal or No Deal Will you be a millionaire")
    start_game = input("press any button to start")
    name = input("\n Please enter your name:  ")
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Player", name])


def shuffler(cases):
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["cases shuffled = True"])
    return shuffle_cases

def select_case(cases_left):
    pass
    # print cases left to user
    # user will input a number between and including 1-22
    # remove selected case from cases_left
    # return selected case back to main

def game(shuffle_cases, cases_left, user_case, count):
    pass
    # loop to remove selected case from cases_left list
    # while loop check if count =< 6
    # print cases_left to user
    # prompt user to enter input 
    # loop to check if input is in cases left
    # 

def banker_offer(cases_left, shuffle_cases):
    pass
    # 

def game_finish(cases_left):
    pass
    # if cases left < 2 return True else False

def double_or_nothing():
    pass
