from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


"""For this assignment, we want to play hangman in 2-player mode.
The game should start by prompting player 1 to pick a word.
Then the screen should clear itself so that player 2 can't see the word
hint: print(chr(27) + "[2J")

After the screen is clear, the "gallows" and the empty letter spaces should be drawn, and player 2 should be allowed 
to guess letters until they either win, or lose. As they choose correct letters, the letters should appear on the 
screen in place of the blank space (clear and redraw the whole screen). As they choose wrong letters, 
the "man" himself should come end up being drawn, piece by piece. How many guesses they get before losing is up to 
you (depending on how complicated of a man you want to draw). """

words = ["judy", "voke"]
picked_word = input("player 1 please pick a word ")
dashes = "_" * len(picked_word)  # displays dashed according to the length of the selected work
# dashes string->list to assign a guessed letter at the corresponding position
dashes_as_list = list(dashes)
print(dashes)

while True:
    guessed_letter = input("guess a letter for player 1  word ")

    # returns a list of index/positions with the guessed letter
    indices = [i for i, letter in enumerate(picked_word) if letter == guessed_letter]

    # loop thru the above list of indices and assign
    # the  guesses letter in their respective positions
    # on the dashes list(dashes_as_list)
    for index in indices:
        dashes_as_list[index] = guessed_letter
    # join the list into a string using the join()
    dashes = "".join(dashes_as_list)
    print(dashes)





