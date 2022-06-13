# this program is a Rock-Paper-Scissors game 
# between computer and human

import random

# function to check validity of input
def isvalid_input(value):
    if (value == "R") or (value =="P") or (value == "S"):
        return True
    return False

# function to output full name
def print_full_name(value):
    if(value == 'P'):
        return 'Paper'
    elif(value == 'R'):
        return 'Rock'
    else:
        return 'Scissors'

# initialize game
options = ['R', 'S', 'P']
cpu = random.choice(options)
cpu.upper()
# print(cpu)
print("Welcome to the Rock-Paper-Scissors game")
print("=======================================")
print("Enter choice with the appropriate letter: \nR is for rock \nP for paper \nS for scissors")
player = input("Enter your choice:")
player = player.upper()
# print(isvalid_input(player))
#TO DO 
# printing names not as symbol

if(isvalid_input(player) == True):
    while(True):
        if(player == cpu):
            print("Player({}) : CPU({})".format(print_full_name(player), print_full_name(cpu)),"It's a tie")
            cpu = random.choice(options)
            # print(cpu)
            print("Enter choice with the appropriate letter: \nR is for rock \nP for paper \nS for scissors")
            player = input("Enter your choice:")
            player = player.upper()
        elif((player == 'R' and cpu == 'S') or (player == 'P' and cpu == 'R') or (player == 'S' and cpu == 'P')):
            print("The choices were: Player({}) : CPU({})".format(print_full_name(player), print_full_name(cpu)))
            print("Player won!")
            break
        else:
            print("The choices were: Player({}) : CPU({})".format(print_full_name(player), print_full_name(cpu)))
            print("CPU won!")
            break
# Handle case for invalid input

elif(isvalid_input(player) == False):
    print("Ivalid input")
    # give user a second chance to enter input
    print("Enter choice with the appropriate letter: \nR is for rock \nP for paper \nS for scissors")
    player = input("Enter your choice:")
    player = player.upper()
    while(True):
        if(player == cpu):
            print("Player({}) : CPU({})".format(print_full_name(player), print_full_name(cpu)),"It's a tie")
            cpu = random.choice(options)
            print(cpu)
            print("Enter choice with the appropriate letter: \nR is for rock \nP for paper \nS for scissors")
            player = input("Enter your choice:")
            player = player.upper()
        elif((player == 'R' and cpu == 'S') or (player == 'P' and cpu == 'R') or (player == 'S' and cpu == 'P')):
            print("The choices were: Player({}) : CPU({})".format(print_full_name(player), print_full_name(cpu)))
            print("Player won!")
            break
        else:
            print("The choices were: Player({}) : CPU({})".format(print_full_name(player), print_full_name(cpu)))
            print("CPU won!")
            break


