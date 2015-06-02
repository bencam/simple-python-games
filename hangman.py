# This is a very basic text-based hangman game





from random import randint


### Generate a random word from the file dictionary.txt ###
# My dictionary.txt file has close to 350,000 words in it (meaning it's hard to win ... )
# Open the dictionary and read it
open('dictionary.txt', 'r').read()

# Turn the file into a list
dictionary = [str(line) for line in open('dictionary.txt')]

# Create a random number and store it in a variable
ran_num = randint(0, (len(dictionary) - 1))

# Select a word in the dictionary list at random
ran_word = dictionary[ran_num]

# Remove the last character of the word (the dictionary.txt file I am using
# has a '/n' character at the end of each word)
ran_word = ran_word[:-1]






### Set up lists and variables ###
# Turn the ran_word string into a list of letters
word = list(ran_word)
avail_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chos_letters = []
correct_guesses = ['_' for x in range(len(ran_word))]
body_parts = ['a head', 'a neck', 'an upper body', 'an arm', 'an arm', 
'a leg', 'a leg', 'a hand', 'a hand', 'a foot', 'a foot', 'a face']
body_parts_count = 0
guess_count = 0
keep_playing = True






### Start the game ###
print 'Welcome to Hangman!'
raw_input('When you\'re readty to start, hit return: ')
print '\nOkay, we\'ve chosen a word, and it\'s %d letters long.' % len(ran_word)
print str(len(ran_word) * '_ ') + '\n'






### Functions ###
# This function finds the index of a character (or characters) in a list
def find_indexes(lst, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = lst.index(item, start_at + 1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

# This function is used to insert correctly-guessed letters
# into the correct_guesses list
def insert_into_list(x, y):
    for integer in x:
		y[integer] = u_letter






### While loop ###
while keep_playing:
	u_letter = raw_input('Please enter a letter: ')
	u_letter = u_letter.lower()
	
	# Handle a letter that is in the word
	if u_letter in word:
		print 'Good guess! The letter ' + u_letter + ' is in our word.'
		chos_letters.extend(u_letter)
		letter_num_of_apperances = word.count(u_letter)
		index = find_indexes(word, u_letter)
		guess_count += 1
		
		# Check to see if the correct letter choice was picked previously
		if u_letter in avail_letters:
			avail_letters.remove(u_letter)
			
			# Handle a letter that appears one time in the word
			if letter_num_of_apperances == 1:
				print 'And it appears one time.'
				insert_into_list(index, correct_guesses)
				
				# Determine if the player has won
				if ran_word == ''.join(correct_guesses):
					print '\nCongratulations! You solved the puzzle.'
					print 'The word was ' + ran_word.upper() + '!'
					print 'You finished the puzzle in ' + str(guess_count) + ' guesses.\n'
					keep_playing = False
				else:
					print 'Here is the word so far: ' + ''.join(correct_guesses)
					print 'Ready to guess again?\n'
			
			# Handle a letter that appears more than one time in the word
			else:
				print 'And it appears ' + str(letter_num_of_apperances) + ' times.'
				insert_into_list(index, correct_guesses)
				
				# Determine if the player has won
				if ran_word == ''.join(correct_guesses):
					print '\nCongratulations! You solved the puzzle.'
					print 'The word was ' + ran_word.upper() + '!'
					print 'You finished the puzzle in ' + str(guess_count) + ' guesses.\n'
					keep_playing = False
				else:
					print 'Here is the word so far: ' + ''.join(correct_guesses)  
					print 'Ready to guess again?\n'
			
		# Handle a correct letter choice that was picked previously
		else:
			print 'But you already guessed that letter.'
			print 'Why don\'t you try again?\n'



	# Handle a letter that was already chosen
	elif u_letter in chos_letters:
		print 'You already guessed that letter.'
		print 'Why don\'t you try again?\n'
		guess_count += 1


    	    
	# Handle a guess that is not in the avail_letters list
	elif u_letter not in avail_letters:
		print 'I\'m sorry, we didn\'t recognize that.'
		print 'Why don\'t you try again?\n'
		guess_count += 1


    	
	# Handle a letter that is not in the word
	else:
		print 'I\'m sorry, ' + u_letter + ' is not in our word.'
		chos_letters.extend(u_letter)
		avail_letters.remove(u_letter)
		print 'We\'ve added ' + body_parts[body_parts_count] + ' to our hangman.'
		guess_count += 1
		body_parts_count += 1
		     
		# Determine if the player has lost
		if body_parts_count == 11:
			print '\nBut we\'re all out of body parts!'
			print 'You lose.'
			print '\nThe word was %s.' % ran_word.upper()
			print 'You made a total of ' + str(guess_count) + ' guesses.'
			print 'Better luck next time ... \n'
			keep_playing = False
		else:
			print 'Here is the word so far: ' + ''.join(correct_guesses)
			print 'Ready to guess again?\n'






