import random

randomnoe_cislo = random.randint(0, 100)

chances = 7

def guess(chances):

    if chances >= 1:
        vvod_cisla = int(input('Введите число: '))
        if vvod_cisla != randomnoe_cislo and vvod_cisla > randomnoe_cislo and chances != 1:
            print('Неправильно, Я загадал меньше. Осталось', chances-1, 'попыток')
            chances -= 1
            guess(chances)
        elif vvod_cisla != randomnoe_cislo and vvod_cisla < randomnoe_cislo and chances != 1:
            print('Неправильно. Я загадал больше. Осталось', chances-1, 'попыток')
            chances -= 1
            guess(chances)
        elif vvod_cisla == randomnoe_cislo:
            print('Правильно. Я загадал ', randomnoe_cislo)
        elif vvod_cisla != randomnoe_cislo and vvod_cisla > randomnoe_cislo and chances == 1:
            print('Ты проиграл. Я загадал', randomnoe_cislo)
        elif vvod_cisla != randomnoe_cislo and vvod_cisla < randomnoe_cislo and chances == 1:
            print('Ты проиграл. Я загадал', randomnoe_cislo)


if __name__ == '__main__':
    guess(chances)
