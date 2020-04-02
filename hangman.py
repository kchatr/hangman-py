import random
from list_of_words import w_list

def choose_word():
    word = random.choice(w_list)
    return word.upper()

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
        if len(guessed_letters) > 0:
            print("\nThe letters you have guessed are: " + " ".join(guessed_letters))
        cur_guess = input("Please guess a letter or word: ").upper() #the current guess
        
        if len(cur_guess) == 1 and cur_guess.isalpha():
            if cur_guess in guessed_letters:
                print("You have already guessed " + cur_guess)
            elif cur_guess not in word:
                print(cur_guess, "is not in the word...")
                guessed_letters.append(cur_guess)
                tries -= 1
            else:
                print("Nice job!", cur_guess, "is in the word!")
                guessed_letters.append(cur_guess)

                word_list = list(word_comp)
                for i in range(0, len(word)):
                    if word[i] == cur_guess:
                        word_list[i] = cur_guess
                
                word_comp = "".join(word_list)
                # for i in range(0, len(word)):
                #     if word[i] == cur_guess:
                #         word_comp
                if "_" not in word_comp:
                    guessed = True
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
        else:
            print("Not a valid guess!")
        print(disp_hangman(tries))
        print(" ".join(word_comp) + "\n")

    if guessed:
        print("Great job! You guessed the word", word, ". You win!")
    else:
        print("Sorry - you ran out of tries. You lose :(")
        print("\nThe word was:", word)



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

def main():
    word = choose_word()
    play(word)
    user = input("Would you like to play again? (Y/N)").upper()
    if user == "N":
        print("Thanks for playing!")
        exit()
    else:
        main()

if __name__ == "__main__":
    main()