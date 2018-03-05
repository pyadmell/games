# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    name = name.capitalize()
    if (name == "Rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "Paper"):
        return 2
    elif (name == "Lizard"):
        return 3
    elif (name == "Scissors"):
        return 4
    else:
        print "name does not match!"
        

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
        if number == 0:
            return "Rock"
        elif number == 1:
            return "Spock"
        elif number == 2:
            return "Paper"
        elif number == 3:
            return "Lizard"
        elif number ==4:
            return "Scissors"
        else:
            print "Number is not in the correct range"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    player_choice = player_choice.capitalize()  
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Playe chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if difference <=2 and difference > 0:
        print "Computer wins!"
    elif difference > 2 and difference <=4:
        print "Player wins!"
    elif difference == 0:
        print "Draw!"
    else:
        print "Error in the program"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


