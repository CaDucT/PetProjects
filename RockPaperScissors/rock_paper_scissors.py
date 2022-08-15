import random

a = ['rock', 'paper', 'scissors']
score_h = 0
score_b = 0
choose = int(input('How long do we play? Put number: '))

def thegame(score_h, score_b):
    if score_b == choose:
        print('The game is over. You lost')
        quit()
    elif score_h == choose:
        print('The game is over. You won')
        quit()
    while score_b <= choose or score_h <= choose:
        ask = input('Choose: Rock, Paper or Scissors? ')
        bot = random.choice(a)
        if ask.lower() == 'rock' and bot == 'paper':
            score_b = score_b + 1
            print('Paper beats rock, you lost. Score: ', score_h, '-', score_b)
            thegame(score_h, score_b)
        elif ask.lower() == 'paper' and bot == 'rock':
            score_h = score_h + 1
            print('Paper beats rock, you won. Score: ', score_h, '-', score_b)
            thegame(score_h, score_b)
        elif ask.lower() == 'rock' and bot == 'scissors':
            score_h = score_h + 1
            print('Rock beats scissors, you won. Score: ', score_h, '-', score_b)
            thegame(score_h, score_b)
        elif ask.lower() == 'scissors' and bot == 'rock':
            score_b = score_b + 1
            print('Scissors beat rock, you lost. Score: ', score_h, '-', score_b)
            thegame(score_h, score_b)
        elif ask.lower() == 'paper' and bot == 'scissors':
            score_b = score_b + 1
            print('Scissors beat paper, you lost. Score: ', score_h, '-', score_b)
            thegame(score_h, score_b)
        elif ask.lower() == 'scissors' and bot == 'paper':
            score_h = score_h + 1
            print('Scissors beat paper , you won. Score: ', score_h, '-', score_b)
            thegame(score_h, score_b)
        elif ask.lower() == bot:
            print('Deuce')
            thegame(score_h, score_b)
        elif ask.lower() == 'stop':
            pass

if __name__ == '__main__':
    thegame(score_h, score_b)