import random
print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hidden = list(len(word) * '-')
tries = 0
guesses = []
answer = ''


def menu():
    global tries, guesses, hidden, word
    tries = 0
    guesses = []
    word = random.choice(words)
    hidden = list(len(word) * '-')
    # noinspection PyShadowingNames
    answer = input('Type "play" to play the game, "exit" to quit:')
    if answer == 'play':
        turn()
    elif answer == 'exit':
        exit()


def turn():
    global tries
    if tries == 8:
        print('You lost!')
        print('')
        exit()
    print('')
    print(''.join(hidden))
    guess = input('Input a letter:')
    while True:
        if len(guess) != 1:
            print('You should input a single letter')
            turn()
        elif not guess.isalpha() or guess.isupper():
            print('Please enter a lowercase English letter')
            turn()
        elif guess in guesses:
            print("You've already guessed this letter")
            turn()
        elif guess in word:
            counter = -1
            for x in word:
                counter += 1
                if guess == x:
                    hidden[counter] = guess
                    guesses.append(guess)
                    if ''.join(hidden) == word:
                        print(word)
                        print('You guessed the word!')
                        print('You survived!')
                        print('')
                        exit()
            turn()
        else:
            tries += 1
            print("That letter doesn't appear in the word")
            guesses.append(guess)
            turn()


while True:
    menu()
