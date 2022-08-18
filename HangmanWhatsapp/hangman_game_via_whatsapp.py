from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
import time
import sys
import random

sys.setrecursionlimit(10000)
ser = Service(r"C:\webdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/nonse/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Profile 3')
driver = webdriver.Chrome(chrome_options=options, service=ser)
driver.maximize_window() # maximize browser's window

def hearing(max_tries, used_words, wrong_tries, random_word, hidden_word):

    time.sleep(2)
    #if used_words != []:
        #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Already used letters: ', used_words, Keys.ENTER)
    guess = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]').text
    guess = guess.strip().split()
    if wrong_tries == max_tries:
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('You lost. The random word is: ', random_word, Keys.ENTER)
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Do you want to play again? Type y or yes or da', Keys.ENTER)
        if guess[-2] == 'Yes' or guess[-2] == 'Y' or guess[2] == 'Da':
            start_game()
        else:
            quit()
    elif hidden_word == random_word:
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('You won. The random word was: ', random_word, Keys.ENTER)
    if guess[-2] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz':
        while wrong_tries < max_tries and hidden_word != random_word:
            if guess[-2] in used_words:
                return hearing(max_tries,used_words,wrong_tries,random_word,hidden_word)
            used_words.append(guess[-2])
            if guess[-2] in random_word:
                driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Yes! The word contains the letter ', guess[-2], Keys.ENTER)
                new = ''
                for i in range(len(random_word)-1):
                    if guess[-2] == random_word[i]:
                        new += guess[-2]
                    else:
                        new += hidden_word[i]
                hidden_word = new
                driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(hidden_word, Keys.ENTER)
            else:
                driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Oops! The wrong letter', Keys.ENTER)
                driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Already used letters: ', used_words, Keys.ENTER)
                wrong_tries += 1
        if len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return hearing(max_tries, used_words,wrong_tries,random_word,hidden_word)

        elif wrong_tries == max_tries:
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('You lost. The random word is: ', random_word, Keys.ENTER)
            gg = input('Do you want to play again? ')
            if gg == 'yes' or gg == 'y' or gg == 'da':
                start_game()
            else:
                quit()
    else:
        time.sleep(1)
        hearing(max_tries, used_words, wrong_tries, random_word, hidden_word)

def glavnoe(max_tries, used_words, wrong_tries, random_word, hidden_word):
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[9]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Hello. This is a hangman game!', Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('The word has ', len(random_word)-1, ' letters. Try to find out the word \n', hidden_word, Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[9]').click()
    hearing(max_tries, used_words, wrong_tries, random_word, hidden_word)

def start_game():
    max_tries = 6
    used_words = []
    wrong_tries = 0
    with open('sowpods.txt', 'r') as file:
        f = file.readlines()
        random_word = random.choice(f)
    hidden_word = '-' * (len(random_word) - 1)
    print('The word has ', len(random_word) - 1, 'letters. Try to find out the word. \n',hidden_word)
    print(random_word)
    glavnoe(max_tries, used_words, wrong_tries, random_word, hidden_word)

start_game()

