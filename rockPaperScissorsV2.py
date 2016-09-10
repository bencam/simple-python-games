# This is a very basic text-based rock-paper-scissors game
# Version 2
# The main difference between version 1 and version 2 is that the latter
# allows the user to choose how many rounds to play


import random


# Determine how many games the user would like to play
print '\nWelcome to the Rock-Paper-Scissors Game.'
print 'How many rounds would you like to play?\n'
print 'Please select:'
print '1 for best out of one round.'
print '2 for best out of three rounds.'
print '3 for best out of five rounds.'
print '4 for best out of seven rounds.'
u_round_selection = int(raw_input('>> '))


# Set variable indicating how many rounds the user wants to play
# This will be used in an if statement for determining if the game is over
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
        print 'I\'m sorry, we didn\'t recognize that.'
        print 'Please select:'
        print '1 for best out of one round.'
        print '2 for best out of three rounds.'
        print '3 for best out of five rounds.'
        print '4 for best out of seven rounds.'
        num = raw_input('>> ')


# Define a function that returns the user's choice
def variable_set_up_user(num):
    if num == 1:
        return 'You chose rock.'
    elif num == 2:
        return 'You chose paper.'
    elif num == 3:
        return 'You chose scissors.'


# Define a function that returns the computer's choice
def variable_set_up_computer(num):
    if num == 1:
        return 'The computer chose rock.'
    elif num == 2:
        return 'The computer chose paper.'
    elif num == 3:
        return 'The computer chose scissors.'


# Set up scoring and round variables
u_score = 0
c_score = 0
rounds_played = 0


# While loop for the playing each round
keep_playing = True
while keep_playing:

    # Print the menu
    print '\nPlease select:'
    print '1 for rock'
    print '2 for paper'
    print '3 for scissors'

    # Get the user's choice and randomly select the computer's choice
    u_choice = int(raw_input('>> '))
    c_choice = random.randint(1, 3)

    # Correct a user choice error
    while u_choice not in [1, 2, 3]:
        print 'You must select rock, paper or scissors. Please select again from the menu below:'
        print '1 for rock'
        print '2 for paper'
        print '3 for scissors'
        u_choice = int(raw_input('>> '))

    # Print user and computer choices
    print ''
    print variable_set_up_user(u_choice)
    print variable_set_up_computer(c_choice)
    rounds_played += 1

    # Determine if it's a tie
    if u_choice == c_choice:
        print 'You tied.'
        print 'The score is still %d (you) - %d (the computer).' % (u_score, c_score)

    # List winning elifs for the user
    elif u_choice == 1 and c_choice == 3:
        print 'Rock beats scissors. You win the round!'
        u_score += 1
        print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)
    elif u_choice == 2 and c_choice == 1:
        print 'Paper beats rock. You win the round!'
        u_score += 1
        print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)
    elif u_choice == 3 and c_choice == 2:
        print 'Scissors beats paper. You win the round!'
        u_score += 1
        print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)

    # List losing elifs for the user
    elif u_choice == 1 and c_choice == 2:
        print 'Paper beats rock. You lose the round.'
        c_score += 1
        print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)
    elif u_choice == 2 and c_choice == 3:
        print 'Scissors beats paper. You lose the round.'
        c_score += 1
        print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)
    elif u_choice == 3 and c_choice == 1:
        print 'Rock beats scissors. You lose the round.'
        c_score += 1
        print 'The score is %d (you) - %d (the computer).' % (u_score, c_score)

    # Determine if the game is over
    if round_selection_var == 1:
        if u_score == 1:
            print 'You win the game!'
            keep_playing = False
        else:
            print 'Sorry, you lose the game.'
            keep_playing = False
    elif round_selection_var == 2:
        if u_score == 2:
            print 'You win the game!'
            keep_playing = False
        elif c_score == 2:
            print 'Sorry, You lose the game.'
            keep_playing = False
        else:
            print 'Ready to guess again?'
    elif round_selection_var == 3:
        if u_score == 3:
            print 'You win the game!'
            keep_playing = False
        elif c_score == 3:
            print 'Sorry, You lose the game.'
            keep_playing = False
        else:
            print 'Ready to guess again?'
    elif round_selection_var == 4:
        if u_score == 4:
            print 'You win the game!'
            keep_playing = False
        elif c_score == 4:
            print 'Sorry, You lose the game.'
            keep_playing = False
        else:
            print 'Ready to guess again?'


# Print how many rounds were played
if rounds_played == 1:
    print 'You played one round.'
else:
    print 'You played a total of ' + str(rounds_played) + ' rounds.'
