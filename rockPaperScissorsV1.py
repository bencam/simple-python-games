#!/usr/bin/env python


"""
This is version 2 of a very basic text-based rock-paper-scissors game.

The object of the game is to choose an object from a list (rock, paper, or
scissors) that 'beats' the object chosen at random (from the same list)
by the computer. The possible game scenarios, with winners indicated, are
as follows:

rock v paper (paper wins)
scissors v paper (scissors wins)
rock v scissors (rock wins)

Note: the primary difference between the two versions of rock-paper-scissors
in this repository is that version 2 allows the user to choose the number of
rounds to play (the user is given the option of a best out of one, three, five
or seven rounds scenario). In version 1, the game always ends after one round.

"""


import random


def menu():
    """Print the menu"""
    print '\nWelcome to the Rock-Paper-Scissors Game'
    print 'Please select:'
    print '1 for rock'
    print '2 for paper'
    print '3 for scissors'


def game():
    """Play the game"""
    # Get the user's choice and randomly select the computer's choice
    u_choice = int(raw_input('>> '))
    c_choice = random.randint(1, 3)

    # Correct a user choice error
    while u_choice not in [1, 2, 3]:
        print 'You must select rock, paper or scissors.'
        print 'Please select again from the menu below:'
        print '1 for rock'
        print '2 for paper'
        print '3 for scissors'
        u_choice = int(raw_input('>> '))

    # Print user and computer choices
    print variable_set_up_user(u_choice)
    print variable_set_up_computer(c_choice)

    # Determine if it's a tie
    if u_choice == c_choice:
        print 'You tied.'

    # If the user won, print the result
    elif u_choice == 1 and c_choice == 3:
        print 'Rock beats scissors. You win!'
    elif u_choice == 2 and c_choice == 1:
        print 'Paper beats rock. You win!'
    elif u_choice == 3 and c_choice == 2:
        print 'Scissors beats paper. You win!'

    # If the user lost, print the result
    elif u_choice == 1 and c_choice == 2:
        print 'Paper beats rock. You lose.'
    elif u_choice == 2 and c_choice == 3:
        print 'Scissors beats paper. You lose.'
    elif u_choice == 3 and c_choice == 1:
        print 'Rock beats scissors. You lose.'


# Helper functions
def variable_set_up_user(num):
    """Return the user's choice"""
    if num == 1:
        return 'You chose rock.'
    elif num == 2:
        return 'You chose paper.'
    elif num == 3:
        return 'You chose scissors.'


def variable_set_up_computer(num):
    """Returns the computer's choice"""
    if num == 1:
        return 'The computer chose rock.'
    elif num == 2:
        return 'The computer chose paper.'
    elif num == 3:
        return 'The computer chose scissors.'


menu()
game()
