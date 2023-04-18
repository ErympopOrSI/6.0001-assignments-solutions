# Problem Set 2, hangman.py
# Name: Olawoyin Temidayo
# Collaborators: None
# Time spent: approx 7 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(words):
    return random.choice(words)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words() 


# A function that helps to check if user has guessed the word
def is_word_guessed(secret_word, letter_guessed):
    return "".join(sorted(set(secret_word))) == "".join(sorted(letter_guessed))

# helps displays the guessed word
def get_guessed_word(secret_word, letters_guessed):
    curr_guess = ""
    for alpha in secret_word:
        if alpha in letters_guessed:
            curr_guess += alpha
        else:
            curr_guess += "_ "
    return curr_guess


# helps display available letters
def get_available_letters(letters_guessed):
    available = ""
    for letter in string.ascii_lowercase:
        if not letter in letters_guessed:
            available += letter
    return available  

def hangman(secret_word):
    # let the game begins
    print("Welcome to the game Hangman !")
    warnings_left = 3

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_left} warnings left\n-------------")
    good_guesses = list()
    total_guess = list()
    guess_left = 6

    vowel = ("a","e","i","o","u")
    consonant = ("b","c","d","f",'g',"h","j",'k','l','m','n','p','q','r','s','t','v','w','x','y','z')

    while True:
        # if user completes the guess
        if is_word_guessed(secret_word, good_guesses):
            print(f"Congratulations, you won!\nYour total score is  {guess_left * len(set(secret_word))}")
            break
        # if out of guess, then game over
        if guess_left < 1:
            print(f"Sorry, you ran out of guesses.The word was {secret_word}")
            break

        ###################### Display information #######################
        print(f"You have {guess_left} guesses left")
        print(f"Available letters: {get_available_letters(total_guess)}")
        ##############################################################

        ##############player's guess ############################################
        player_guess = input("Please guess a letter: ")

        if not player_guess.isalpha():
            if warnings_left:
                print(f"Oops! That is not a valid letter. You have {warnings_left - 1} warnings left\n-------------")
                warnings_left -= 1
            else:
                print(f"\nOops! That is not a valid letter. You have {warnings_left} so you lose one guess\n-------------")
                guess_left -= 1
            continue    
        
        player_guess = player_guess.lower()
        ############################################################

        ####################### if guess not in secret word ################################

        if not player_guess in secret_word:
            if not player_guess in total_guess:
                if player_guess in consonant:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    guess_left -= 1
                    total_guess.append(player_guess)
                elif player_guess in vowel:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    guess_left -= 2
                    total_guess.append(player_guess)
            else:
                if warnings_left:
                    print(f"Oops! you've already guessed this. You have {warnings_left - 1} warnings left: {get_guessed_word(secret_word, good_guesses)}")
                    warnings_left -= 1
                else:
                    print(f"Oops! you've already guessed this. You have {warnings_left} warnings left so you lose one guess: {get_guessed_word(secret_word, good_guesses)}")
                    guess_left -= 1
            continue
        ##############################################################################

        ########## so if guess in secret word #################################

        if player_guess in secret_word:
            if not player_guess in total_guess:
                good_guesses.append(player_guess)
                total_guess.append(player_guess)
                print(f"Good guess: {get_guessed_word(secret_word, good_guesses)}\n-------------")
            else:
                if warnings_left:
                    print(f"You've already guessed that letter. You have {warnings_left - 1} warnings left: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    warnings_left -= 1
                else:
                    print(f"You've already guessed that letter. You have {warnings_left} warning left so you lose one guess: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    guess_left -= 1

        #######################################################################
            
   
# hangman(choose_word(load_words()))

def match_with_gaps(my_word, other_word):
    my_word = my_word.replace("_ ", "*") # replace (_ ) with an asterisk.
    word_len = len(my_word)
    
    duplicate_check = list() # Remember that when a letter is guessed, your code reveals all the positions at which that letter occurs in the secret word. Therefore, the hiddden letter (_ ) cannot be one of the letters in the word that has already been revealed.

    if word_len != len(other_word):
        return False
    
    for n in range(word_len):
        if my_word[n] == "*":
            duplicate_check.append(other_word[n])
        elif my_word[n] != other_word[n]:
            return False
    
    ######## dealing with duplicates ###############
    for n in other_word:
        if n in duplicate_check and n in my_word:
            return False
    return True
    ################################################
    # will modify that one later.


def show_possible_matches(my_word):
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=" ")

def hangman_with_hints(secret_word):
    # let the game begins
    print("Welcome to the game Hangman!")
    warnings_left = 3

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_left} warnings left\n-------------")
    good_guesses = list()
    total_guess = list()
    guess_left = 6

    vowel = ("a","e","i","o","u")
    consonant = ("b","c","d","f",'g',"h","j",'k','l','m','n','p','q','r','s','t','v','w','x','y','z')

    while True:
        # if user completes the guess
        if is_word_guessed(secret_word, good_guesses):
            print(f"Congratulations, you won!\nYour total score is  {guess_left * len(set(secret_word))}")
            break
        # if out of guess, then game over
        if guess_left < 1:
            print(f"Sorry, you ran out of guesses.The word was {secret_word}")
            break

        ###################### Display information #######################
        print(f"You have {guess_left} guesses left")
        print(f"Available letters: {get_available_letters(total_guess)}")
        ##############################################################

        ##############player's guess ############################################
        player_guess = input("Please guess a letter: ")

        # ###### Show hint ##########################

        if player_guess == "*":
                print("Possible matches are \n")
                show_possible_matches(get_guessed_word(secret_word, good_guesses))
                print("\n-------------")
                continue
        
        #############################################
        if not player_guess.isalpha():
            if warnings_left:
                print(f"Oops! That is not a valid letter. You have {warnings_left - 1} warnings left\n-------------")
                warnings_left -= 1
            else:
                print(f"\nOops! That is not a valid letter. You have {warnings_left} so you lose one guess\n-------------")
                guess_left -= 1
            continue    
        
        player_guess = player_guess.lower()

        ############################################################

        ####################### if guess not in secret word ################################

        if not player_guess in secret_word:
            if not player_guess in total_guess:
                if player_guess in consonant:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    guess_left -= 1
                    total_guess.append(player_guess)
                elif player_guess in vowel:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    guess_left -= 2
                    total_guess.append(player_guess)
            else:
                if warnings_left:
                    print(f"Oops! you've already guessed this. You have {warnings_left - 1} warnings left: {get_guessed_word(secret_word, good_guesses)}")
                    warnings_left -= 1
                else:
                    print(f"Oops! you've already guessed this. You have {warnings_left} warnings left so you lose one guess: {get_guessed_word(secret_word, good_guesses)}")
                    guess_left -= 1
            continue
        ##############################################################################

        ########## so if guess in secret word #################################

        if player_guess in secret_word:
            if not player_guess in total_guess:
                good_guesses.append(player_guess)
                total_guess.append(player_guess)
                print(f"Good guess: {get_guessed_word(secret_word, good_guesses)}\n-------------")
            else:
                if warnings_left:
                    print(f"You've already guessed that letter. You have {warnings_left - 1} warnings left: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    warnings_left -= 1
                else:
                    print(f"You've already guessed that letter. You have {warnings_left} warning left so you lose one guess: {get_guessed_word(secret_word, good_guesses)}\n-------------")
                    guess_left -= 1

        #######################################################################

hangman_with_hints(choose_word(wordlist))