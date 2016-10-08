#!/usr/bin/env python

# This is a very basic text-based rock-paper-scissors game
# Version 2
# The main difference between version 1 and version 2 is that the latter
# allows the user to choose how many rounds to play

import random


def print_main_menu():
    """Print the main menu, which prompts a user
    to select how many rounds they would like to play"""
    print 'How many rounds would you like to play?'
    print 'Please select:'
    print '1 for best out of one round.'
    print '2 for best out of three rounds.'
    print '3 for best out of five rounds.'
    print '4 for best out of seven rounds.'


def print_sub_menu():
    """Print the sub menu, which prompts a user to
    choose rock, paper or scissors"""
    print '\nPlease select:'
    print '1 for rock'
    print '2 for paper'
    print '3 for scissors'


def choose_rps():
    """Allow the user to choose rock, paper or scissors"""
    u_choice = int(raw_input('>> '))
    while u_choice not in [1, 2, 3]:
        print 'You must select rock, paper or scissors. Please try again.'
        print_sub_menu()
        u_choice = int(raw_input('>> '))
    return u_choice


def variable_set_up_user(num):
    """Return the user's choice"""
    if num == 1:
        return 'You chose rock.'
    elif num == 2:
        return 'You chose paper.'
    elif num == 3:
        return 'You chose scissors.'


def variable_set_up_computer(num):
    """Return the computer's choice"""
    if num == 1:
        return 'The computer chose rock.'
    elif num == 2:
        return 'The computer chose paper.'
    elif num == 3:
        return 'The computer chose scissors.'


def num_of_rounds():
    """Determine how many games the user would like to play"""
    print '\nWelcome to the Rock-Paper-Scissors Game.'
    print_main_menu()
    u_round_selection = int(raw_input('>> '))

    # Set variable indicating how many rounds the user wants to play
    round_selection_var = 0

    # While loop for round selection
    keep_selecting = True
    while keep_selecting:
        if u_round_selection == 1:
            print 'Alright, best out of one round it is.'
            round_selection_var = 1
            keep_selecting = False

        elif u_round_selection == 2:
            print 'Alright, best out of three rounds it is.'
            round_selection_var = 2
            keep_selecting = False

        elif u_round_selection == 3:
            print 'Alright, best out of five rounds it is.'
            round_selection_var = 3
            keep_selecting = False

        elif u_round_selection == 4:
            print 'Alright, best out of seven rounds it is.'
            round_selection_var = 4
            keep_selecting = False

        else:
            print 'Sorry, that\'s not an option.'
            print_main_menu()
            u_round_selection = int(raw_input('>> '))

    return round_selection_var


def print_score(u_score, c_score):
    """Print the score"""
    print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)


def play_game():
    """Execute the game"""
    # Set up scoring and round variables
    u_score = 0
    c_score = 0
    rounds_played = 0
    rounds = num_of_rounds()

    # While loop for the playing each round
    keep_playing = True
    while keep_playing:
        print_sub_menu()

        # Get the user's choice and randomly select the computer's choice
        u_choice = choose_rps()
        c_choice = random.randint(1, 3)

        # Print user and computer choices
        print ''
        print variable_set_up_user(u_choice)
        print variable_set_up_computer(c_choice)
        rounds_played += 1

        # Determine who won the round
        if u_choice == c_choice:
            print 'You tied.'
        elif u_choice == 1 and c_choice == 3:
            print 'Rock beats scissors. You won the round!'
            u_score += 1
        elif u_choice == 2 and c_choice == 1:
            print 'Paper beats rock. You won the round!'
            u_score += 1
        elif u_choice == 3 and c_choice == 2:
            print 'Scissors beats paper. You won the round!'
            u_score += 1
        elif u_choice == 1 and c_choice == 2:
            print 'Paper beats rock. You lose the round.'
            c_score += 1
        elif u_choice == 2 and c_choice == 3:
            print 'Scissors beats paper. You lose the round.'
            c_score += 1
        elif u_choice == 3 and c_choice == 1:
            print 'Rock beats scissors. You lose the round.'
            c_score += 1

        # Print the score
        print_score(u_score, c_score)

        # Determine if the game is over
        if rounds == 1:
            if u_score == 1:
                print 'You won the game!'
                keep_playing = False
            else:
                print 'Sorry, you lose the game.'
                keep_playing = False
        elif rounds == 2:
            if u_score == 2:
                print 'You won the game!'
                keep_playing = False
            elif c_score == 2:
                print 'Sorry, You lose the game.'
                keep_playing = False
            else:
                print 'Ready to guess again?'
        elif rounds == 3:
            if u_score == 3:
                print 'You won the game!'
                keep_playing = False
            elif c_score == 3:
                print 'Sorry, You lose the game.'
                keep_playing = False
            else:
                print 'Ready to guess again?'
        elif rounds == 4:
            if u_score == 4:
                print 'You won the game!'
                keep_playing = False
            elif c_score == 4:
                print 'Sorry, You lose the game.'
                keep_playing = False
            else:
                print 'Ready to guess again?'

        # Print how many rounds were played
        if rounds_played == 1:
            print 'You\'ve played one round.'
        else:
            print 'You\'ve played a total of ' +\
                str(rounds_played) + ' rounds.'


play_game()
