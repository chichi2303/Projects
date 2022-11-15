import random

numDigs = 3
maxGuesses = 10


def main():
    print('''Bagels, a deductive logicgame.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit numbers with no repeated digits. 
    Try to guess what it is. Here are some clues: 
    When I say:      That means: 
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position
    Bagles          No digit is correct.'''.format(numDigs))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it'.format(maxGuesses))

        numGuesses = 1
        while numGuesses <= maxGuesses:
            guess = ''
            while len(guess) != numDigs or not guess.isdecimal():  # check if length is not == number of digits we expected or if it is not decimal number --> only procced if satisfy
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > maxGuesses:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(numDigs):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == "__main__":
    main()
