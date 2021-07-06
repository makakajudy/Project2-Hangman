import random
from dictionary import word_list


def get_word():
    word_chosen = random.choice(word_list)
    return word_chosen.lower()


def play(picked_word):
    dashes = "_" * len(picked_word)  # displays dashed according to the length of the selected work
    # dashes string->list to assign a guessed letter at the corresponding position
    dashes_as_list = list(dashes)
    tries = 7
    word_guessed = False # initially guessed word is set to False.resets to True when the word is guessed correct
    guessed_letters=[] # list of the guessed letter

    print("Let's play Hangman!")
    player = int(input("please select a player: "))
    print(display_hangman(tries))  # image for the game
    print(dashes)

    while not word_guessed and tries > 0:
        if player == 1:
            guessed_letter = input(f"player {player}  please guess a letter for player 2's  word ").lower()
        else:
            guessed_letter = input(f"player {player}  please guess a letter for player 1's  word ").lower()

        if len(guessed_letter) == 1 and guessed_letter.isalpha():  # for single alphabet entry
            if guessed_letter in guessed_letters:
                print("you already guessed this letter")
                print(f"my guess list so far{guessed_letters}")

            elif guessed_letter not in picked_word and guessed_letter not in guessed_letters:
                print(f" {guessed_letter} not in the word. try again")
                guessed_letters.append(guessed_letter)
                print(display_hangman(tries))

            else:
                print("Bingo,the letter is in the word!")
                guessed_letters.append(guessed_letter)
                indices = [i for i, letter in enumerate(picked_word) if letter == guessed_letter]  # returns a list of
                # index/positions with the guessed letter
                for index in indices:  # loop through the above list of indices
                    dashes_as_list[
                        index] = guessed_letter  # and assign,the  guesses letter in their respective positions
                # on the dashes list(dashes_as_list)
                dashes = "".join(dashes_as_list)  # join the list into a string using the join()
                print(dashes)
                if "_" not in dashes:  # if dashes are filled set word_guessed to True
                    word_guessed = True

        elif len(guessed_letter) == len(picked_word) and guessed_letter.isalpha():  # for whole word entry
            if guessed_letter == picked_word:
                word_guessed = True
                print("right on spot")
            else:
                print("that's not the correct word try again")
                print(display_hangman(tries))

        else:
            print("invalid entry try again")
            print(display_hangman(tries))

        tries -= 1
    if word_guessed:
        print("well done")
    else:
        print("you have run out of tries")
        print(f"{word} was the word")


def display_hangman(tries):
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
        # head and neck
        """
                   --------
                   |      |
                   |      O
                   |      |    
                   |      
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


word = get_word()
# word = input("player 1 please pick a word ")
play(word)
play_again=input("would you like to play again (y/n)?")
if play_again!="n" :
    word = get_word()
    play(word)
else:
    print(" Game over")







