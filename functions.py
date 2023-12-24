import random
import csv
from colored import fg, attr
import subprocess
import math


class EmptyInputError(Exception):
    pass


class InvalidStringError(Exception):
    pass


class InvalidIntegerError(Exception):
    pass


class YesOrNoInputError(Exception):
    pass


# usage for colored is as follows
# {specify colour change}  (text or variable that we want to change color)  {attr('reset') to reset terminal color to default}

color_heading: str = f"{attr(1)}{fg(4)}"
color_text: str = f"{attr(3)}{fg(15)}"
color_your_case: str = f"{attr(3)}{fg(188)}"
color_cases_left: str = f"{attr(3)}{fg(11)}"
color_money_left: str = f"{attr(1)}{fg(10)}"
color_input_error: str = f"{attr(4)}{fg(1)}"
color_winnings: str = f"{attr(3)}{fg(220)}"


file = "gamelog.csv"


def game_menu():
    # clears the screen
    try:
        subprocess.run("clear")
    except:
        subprocess.run("cls")
    print(
        f"{color_heading}Welcome to Deal or No Deal Will you take home the top prize?{attr('reset')}"
    )
    start_game = input(
        f"\n{color_heading}Enter H to view how to play\n\nPress Enter to start the game... {attr('reset')}"
    )
    if start_game.lower() == "h":
        game_help()
    while True:
        try:
            name = input(f"\n{color_text}Please enter your name:  {attr('reset')}")
            if len(name) > 0:
                if all(letter.isalpha() or letter.isspace() for letter in name):
                    break
                raise InvalidStringError("Invalid characters")
            raise EmptyInputError("Empty String")

        except InvalidStringError:
            print(
                f"\n{color_input_error}Your name can only contain characters from a-z{attr('reset')}"
            )
        except EmptyInputError:
            print(
                f"\n{color_input_error}Your name must contain at least 1 character{attr('reset')}"
            )
        except Exception as e:
            print(f"{color_input_error}Unexpected Error: {e}{attr('reset')}")

    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Player", name])


def game_help():
    print(f"{color_heading}\nWelcome to Deal or No Deal how to play{attr('reset')}")
    print(
        "deal or no deal has 22 cases to begin with various values ranging from $1 to $200000",
        "you will choose one case that you think has high value",
        "you will slowly open the cases until the bank makes you an offer",
        "the objective is to open all the low value cases so the bank will offer you more money",
        "if you accept a bank offer, the bank will also offer you a 50/50 chance to double your money",
        )


def shuffler(cases):
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["cases shuffled = True\n"])
        for key, value in shuffle_cases.items():
            writer.writerow([key, value])
    return shuffle_cases


def select_case():
    cases_left = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
    ]
    # print cases left to user
    try:
        subprocess.run("clear")
    except:
        subprocess.run("cls")
    
    print(color_cases_left, *cases_left, attr("reset"))
    # user will input a number between and including 1-22
    while True:
        try:
            user_case = int(
                input(f"\n{color_text}Please Select your lucky case:  {attr('reset')}")
            )
            if user_case <= 22 and user_case >= 1:
                break
            raise InvalidIntegerError("Invalid integer")
        
        except ValueError:
            print(f"{color_input_error}Please enter an integer{attr('reset')}")

        except InvalidIntegerError:
            print(f"{color_input_error} enter a valid integer between 1-22{attr('reset')}")
        
        except Exception as e:
            print(f"{color_input_error}Unexpected Error: {e}{attr('reset')}")

    # remove selected case from cases_left
    for case in cases_left:
        if user_case == case:
            cases_left.remove(case)
            break
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Users_case", user_case])
        writer.writerow(["case_removed", user_case])
    # return selected case back to main
    return user_case, cases_left


def banker_offer(nums, nums_left, user_num):
    # Median square root calculator / Quadratic mean calculator
    total_money_left = 0
    for key, value in nums.items():
        if key in nums_left or key == user_num:
            total_money_left = total_money_left + math.pow(value, 2)
    offer = (math.sqrt((total_money_left / (len(nums_left) + 1))))
    return offer


def game(cases, shuffle_cases, cases_left, user_case):
    interation = 0
    while interation < 6:
        count = 6 - int(interation)
        # while loop check if count =< 0
        while count != 0:
            # clears the screen
            try:
                subprocess.run("clear")
            except:
                subprocess.run("cls")
            # print cases_left to user
            print(
                f"\n{color_text}Money Left:{attr('reset')}",
                color_money_left,
                *cases.values(),
                attr("reset"),
            )
            print(
                f"\n{color_text}Cases Left to open: {attr('reset')}",
                color_cases_left,
                *cases_left,
                attr("reset"),
            )
            print(
                f"\n{color_text}Your Lucky Case Is:  {attr('reset')}",
                color_your_case,
                [user_case],
                attr("reset"),
            )
            try:
                print(
                    f"{color_text}The last Case opened: No. ",
                    color_cases_left,
                    rm_case,
                    attr("reset"),
                    f"{color_text}contained: {attr('reset')}",
                    color_money_left,
                    "$",
                    rm_value,
                    attr("reset"),
                )
            except:
                print("")
            print(f"{color_text}Next bank offer in: {count} cases{attr('reset')}")
            # ask user to enter a case to be removed
            while True:
                try:
                    tobe_removed = int(
                        input(f"\n{color_text}Please select a Case to be removed:  ")
                    )
                    if tobe_removed in cases_left:
                        break
                    raise InvalidIntegerError("Invalid Integer")
                except ValueError:
                    print(
                        f"{color_input_error}Please enter a valid integer{attr('reset')}"
                    )
                except InvalidIntegerError:
                    print(
                        f"{color_input_error}Please choose a number from the cases left to open{attr('reset')}"
                    )
                except Exception as e:
                    print(
                        f"{color_input_error}Unexpected Error: {e}{attr('reset')}"
                    )
                    
            # remove case from cases left
            for case in cases_left:
                if case == tobe_removed:
                    rm_case = case
                    cases_left.remove(case)
                    break
            else:
                continue
            # to print value of removed case to user
            for key, value in shuffle_cases.items():
                if key == tobe_removed:
                    rm_value = value
                    break
            else:
                continue
            # remove value from game
            for key, value in cases.items():
                if value == rm_value:
                    cases.pop(key)
                    break
            else:
                continue
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["case_removed", rm_case])
            count -= 1
        try:
            subprocess.run("clear")
        except:
            subprocess.run("cls")
        # Calculates the Median Square Root
        banks_offer = banker_offer(shuffle_cases, cases_left, user_case)
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["Bank Offer", (interation + 1), int(banks_offer)])
        print(
            f"\n{color_text}Money Left:{attr('reset')}",
            color_money_left,
            *cases.values(),
            attr("reset"),
        )
        print(
            f"\n{color_text}Cases Left to open: {attr('reset')}",
            color_cases_left,
            *cases_left,
            attr("reset"),
        )
        print(
            f"\n{color_text}Your Lucky Case Is:  {attr('reset')}",
            color_your_case,
            [user_case],
            attr("reset"),
        )
        try:
            print(
                f"{color_text}The last Case opened: No. ",
                color_cases_left,
                rm_case,
                attr("reset"),
                f"{color_text}contained: {attr('reset')}",
                color_money_left,
                "$",
                rm_value,
                attr("reset"),
            )
        except:
            print("")
        # prints bank offer
        print(
            f"\n{color_text}The Bank is willing to offer you{attr('reset')}",
            color_money_left,
            "$",
            int(banks_offer),
            attr("reset"),
        )
        user_input = yesorno()
        if user_input.lower() in ("yes", "y"):
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["Bank Offer Accepted"])
            user_input_yes = "yes"
            interation = 6
        else:
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["Bank Offer Declined"])
            user_input_yes = "no"
            interation += 1
        if len(cases_left) == 1:
            interation += 6
    return user_input_yes, banks_offer


def double_or_nothing(user_case, shuffle_cases, user_input_yes, banks_offer):
    try:
        subprocess.run("clear")
    except:
        subprocess.run("cls")
    for key, value in shuffle_cases.items():
        if key == user_case:
            user_case_value = value
            break
    try:
        if user_input_yes == "yes":
            print(
                f"\n{color_text} The bank wishes to make you one last offer\n You can accept: {attr('reset')}",
                color_money_left,
                "$",
                int(banks_offer),
                attr("reset"),
                "\n\nOr Risk it all for a 50/50 chance to win ",
                color_money_left,
                "$",
                (int(banks_offer) * 2),
                attr("reset"),
            )
            double_chance = yesorno()
            if double_chance == "y" or double_chance == "yes":
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Double or nothing offer Accepted"])
                print(
                    f"\n{color_cases_left}   [1]      [2]    {attr('reset')}\n\n {color_text}You have a 50/50 Chance of doubling your money{attr('reset')}"
                )
                while True:
                    try:
                        case_choice = int(
                            input(
                                f"\n{color_text}Please Select your between case 1 and case 2   {attr('reset')}"
                            )
                        )
                        if case_choice <= 2 and user_case >= 1:
                            break
                        raise InvalidIntegerError("Only 1 or 2")
                    except ValueError:
                        print(
                            f"{color_input_error}Please enter an integer{attr('reset')}"
                        )
                    except InvalidIntegerError:
                        print(
                            f"{color_input_error}Please enter 1 or 2 {attr('reset')}"
                        )
                money = [0, (banks_offer * 2)]
                winnings = int(random.choice(money))
                if winnings > 0:
                    print(
                        f"{color_winnings}Congratulations you Won {attr('reset')}{color_money_left}${winnings}{attr('reset')}"
                    )
                else:
                    print(
                        f"{color_winnings}Sorry your gamble didn't pay off you won  {attr('reset')}{color_money_left}${winnings}{attr('reset')}"
                    )
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    if winnings > banks_offer:
                        writer.writerow(["Won Double YAY!"])
                    else:
                        writer.writerow(["Walking away with nothing"])
                play_again = input(
                    f"{color_text}Would you like to play again?  {attr('reset')}"
                ).lower()
            else:
                print(
                    f"{color_winnings}Congratulations you won {attr('reset')}{color_money_left}${banks_offer}{attr('reset')}"
                )
                play_again = input(
                    f"{color_text}Would you like to play again?  {attr('reset')}"
                ).lower()
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Double or nothing Declined"])
                    writer.writerow(["won", banks_offer])
        else:
            print(
                f"{color_winnings}Congratulations your case {attr('reset')}{color_cases_left}{user_case} {attr('reset')}{color_text}contained{attr('reset')}{color_money_left} ${user_case_value}{attr('reset')}"
            )
            play_again = input(
                f"{color_text}Would you like to play again?  {attr('reset')}"
            ).lower()
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["won", user_case_value])
    except:
        print(
            f"{color_winnings}Congratulations your case {attr('reset')}{color_cases_left}{user_case} {attr('reset')}{color_text}contained{attr('reset')}{color_money_left} ${user_case_value}{attr('reset')}"
        )
        play_again = input(
            f"{color_text}Would you like to play again?  {attr('reset')}"
        ).lower()
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["won", user_case_value])
    return play_again


def yesorno():
    while True:
        try:
            user_input = input(
                f"{color_text}\nDo you accept this offer?: {attr('reset')}"
            )
            if len(user_input) > 0:
                if all(
                    letter.isalpha() or letter.isspace() for letter in user_input):
                    if user_input.lower() in ("y", "yes", "n", "no"):
                        break
                    raise YesOrNoInputError("Invalid answer")
                raise InvalidStringError("invalid string")
            raise EmptyInputError("empty string")
        except EmptyInputError:
            print(
                color_input_error,
                "Please enter yes or no",
                attr("reset"),
            )
        except InvalidStringError:
            print(
                color_input_error,
                "Invalid input Please answer Yes or No",
                attr("reset"),
            )
        except YesOrNoInputError:
            print(
                    color_input_error,
                    "Please Answer Yes or No", 
                    attr("reset"),
                )
    return user_input


def game_finish(play_again):
    if play_again == "yes" or play_again == "y":
        exit = True
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["User playing again"])
    else:
        exit = False
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["User exiting application"])
    return exit
