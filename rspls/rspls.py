__author__ = 'yan'

# rock-paper-scissors-lizard-Spock

# encode roles with numbers
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def number2Name(num):
    if num == 0 :
        return "rock"
    elif num == 1 :
        return "Spock"
    elif num == 2 :
        return "paper"
    elif num == 3 :
        return "lizard"
    elif num == 4 :
        return "scissors"
    else :
        print (str(num)+"cannot decode into any role")

def name2Number(name):
    if name == "rock" :
        return 0
    elif name == "Spock" :
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" :
        return 3
    elif name == "scissors" :
        return 4

def rpsls(name):
    num_of_player = name2Number(name)
    random.seed()
    num_of_computer = random.randrange(0,4,1)

    role_of_player = name
    role_of_computer = number2Name(num_of_computer)

    print("player acts "+role_of_player)
    print("computer acts "+ role_of_computer)

    if (num_of_player - num_of_computer)%5>0 and (num_of_player - num_of_computer)%5<=2 :
        player_win = True
        print("player wins")
    elif (num_of_player - num_of_computer)%5<=4 and (num_of_player - num_of_computer)%5>2 :
        player_win = False
        print("computer wins")
    elif num_of_player == num_of_computer:
        print("even")
        player_win = False
    else :
        print("logical error")
        player_win = False

    return player_win




# test rpsls(name)
if_players_wins = rpsls("rock")
if_players_wins = rpsls("Spock")
if_players_wins = rpsls("paper")
if_players_wins = rpsls("lizard")
if_players_wins = rpsls("scissors")







