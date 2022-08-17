import random

def hangmangame(max_tries, used_words, wrong_tries, random_word, hidden_word):
    if used_words != []:
        print('Already used letters: ', used_words)
    guess = input('Let\'s guess the letter: ')
    guess = guess.upper()

    while wrong_tries < max_tries and hidden_word != random_word:
        if guess in used_words:
            return hangmangame(max_tries,used_words,wrong_tries,random_word,hidden_word)
        used_words.append(guess)
        if guess in random_word:
            print('Yes! The word contains the letter', guess)
            new = ''
            for i in range(len(random_word)-1):
                if guess == random_word[i]:
                    new += guess
                else:
                    new += hidden_word[i]
            hidden_word = new
            print(hidden_word)
        else:
            print('Oops! The wrong letter')
            wrong_tries += 1
    if len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return hangmangame(max_tries, used_words,wrong_tries,random_word,hidden_word)
    elif wrong_tries == max_tries:
        print('You lost. The random word is: ', random_word)
        gg = input('Do you want to play again? ')
        if gg == 'yes' or gg == 'y' or gg == 'da':
            used_words = []
            wrong_tries = 0
            start_game()
        else:
            quit()


def start_game():
    max_tries = 6
    used_words = []
    wrong_tries = 0
    with open('sowpods.txt', 'r') as file:
        f = file.readlines()
        random_word = random.choice(f)
    hidden_word = '*' * (len(random_word) - 1)
    print('The word has ', len(random_word) - 1, 'letters. Try to find out the word. \n',hidden_word)
    print(random_word)
    hangmangame(max_tries, used_words, wrong_tries, random_word, hidden_word)

start_game()