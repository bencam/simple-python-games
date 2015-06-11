# This is a very basic text-based hangman game
# Version 1




import random


# Print the menu
print 'Welcome to the Rock, Paper, Scissors Game'
print 'Please select:'
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


# Print user and computer choices
print variable_set_up_user(u_choice)
print variable_set_up_computer(c_choice)


# Determine if it's a tie
if u_choice == c_choice:
    print 'You tied.'


# List winnning elifs for the user
elif u_choice == 1 and c_choice == 3:
    print 'Rock beats scissors. You win!'
elif u_choice == 2 and c_choice == 1:
    print 'Paper beats rock. You win!'
elif u_choice == 3 and c_choice == 2:
    print 'Scissors beats paper. You win!'


# List losing elifs for the user
elif u_choice == 1 and c_choice == 2:
    print 'Paper beats rock. You lose.'
elif u_choice == 2 and c_choice == 3:
    print 'Scissors beats paper. You lose.'
elif u_choice == 3 and c_choice == 1:
    print 'Rock beats scissors. You lose.'





