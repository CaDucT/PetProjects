import random

randomn_number = random.randint(0, 100)

chances = 7

def guess(chances):

    if chances >= 1:
        entered_number = int(input('Enter the number: '))
        if entered_number != randomn_number and entered_number > randomn_number and chances != 1:
            print('Wrong. My number is lower than yours.', chances-1, 'tries left')
            chances -= 1
            guess(chances)
        elif entered_number != randomn_number and entered_number < randomn_number and chances != 1:
            print('Wrong. My number is greater than yours.', chances-1, 'tries left')
            chances -= 1
            guess(chances)
        elif entered_number == randomn_number:
            print('You are right. My number is ', randomn_number)
        elif entered_number != randomn_number and entered_number > randomn_number and chances == 1:
            print('You lost. My number is', randomn_number)
        elif entered_number != randomn_number and entered_number < randomn_number and chances == 1:
            print('You lost. My number is', randomn_number)


if __name__ == '__main__':
    guess(chances)
