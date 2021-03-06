import random
from list_of_words import w_list
"""
Chooses a word randomly from the words list (contains 450 words) and returns it with all uppercase.
"""
def choose_word():
    word = random.choice(w_list)
    return word.upper()
"""
This is responsible for handling all the game's logic and state manipulation, and is the functions which initalizes and executes the game instructions.
"""
def play(word):
    word_comp = "_" * len(word)
    guessed = False
    guessed_letters = [] #keeps track of letters that have been guessed
    guessed_words = [] #keeps track of words that have been guessed
    tries = 6 #number of tries

    print("Let's play a game of Hangman!")
    print(disp_hangman(tries))
    print(" ".join(word_comp) + "\n")
    
    while not guessed and tries > 0:
        #shows the letters that have already been guessed
        if len(guessed_letters) > 0:
            print("\nThe letters you have guessed are: " + ", ".join(guessed_letters))
        cur_guess = input("Please guess a letter or word: ").upper() #the current guess
        
        #if the guess is a letter
        if len(cur_guess) == 1 and cur_guess.isalpha():
            if cur_guess in guessed_letters:
                print("You have already guessed " + cur_guess)
            elif cur_guess not in word:
                print(cur_guess, "is not in the word...")
                guessed_letters.append(cur_guess)
                tries -= 1
            else:
                print("Nice job! The letter", cur_guess, "is in the word!")
                guessed_letters.append(cur_guess)

                word_list = list(word_comp)
                #finds location(s) of letter in word
                for i in range(0, len(word)):
                    if word[i] == cur_guess:
                        word_list[i] = cur_guess
                
                #updates word_comp to display updates
                word_comp = "".join(word_list)
                if "_" not in word_comp:
                    guessed = True
        #if the guess is a word
        elif len(cur_guess) == len(word) and cur_guess.isalpha():
            if cur_guess in guessed_words:
                print("You have already guessed " + cur_guess)
            elif cur_guess != word:
                print(cur_guess, "is not the word")
                tries -= 1
                guessed_words.append(cur_guess)
            else:
                guessed = True
                word_comp = cur_guess
        #invalid response handler
        else:
            print("Not a valid guess!")
        
        print(disp_hangman(tries))
        print(" ".join(word_comp) + "\n")

    if guessed:
        print("Great job! You guessed the word", word, ". You win!")
    else:
        print("Sorry - you ran out of tries. You lose :(")
        print("\nThe word was:", word)


"""
The function which displays the visual state of the game (i.e. how many tries are left).
The ASCII art is stored in a list, with the index of each associated with the number of tries
"""
def disp_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

"""
The function the user directly interacts with and is the abstraction of the logic.
It is a recusrive function in order to handle repeated plays.
"""
def main():
    word = choose_word()
    play(word)
    user = input("Would you like to play again? (Y/N)").upper()
    if user == "N":
        print("Thanks for playing!")
        exit()
    else:
        main()
        print("\n")

if __name__ == "__main__":
    main()