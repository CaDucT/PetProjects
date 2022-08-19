from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import random


sys.setrecursionlimit(10000)
ser = Service(r"C:\browserdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/uie56306/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Profile 3')
driver = webdriver.Chrome(chrome_options=options, service=ser)
driver.maximize_window() # maximize browser's window

def hearing(max_tries, used_words, wrong_tries, random_word, hidden_word):

    while True:
        time.sleep(2)
        guess = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]').text
        guess = guess.strip().split()
        print('Now I\'m in While True cycle')
        if guess[-2] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz':
            print('I\'m breaking the while true cycle so you can continue')
            break

    if guess[-2] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz':

        if wrong_tries == max_tries:
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('You lost. The random word is: ', random_word, Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Do you want to play again? Type Y or Yes or Da', Keys.ENTER)
            time.sleep(10)
            guess = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]').text
            guess = guess.strip().split()
            if guess[-2] == 'Yes' or guess[-2] == 'Y' or guess[2] == 'Da':
                start_game()
            else:
                quit()
        if hidden_word == random_word:
            print('I am in If condition now')
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('You won. The word was: ', random_word, Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Do you want to play again? Type Y or Yes or Da', Keys.ENTER)
            time.sleep(10)
            guess = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]').text
            guess = guess.strip().split()
            if guess[-2] == 'Yes' or guess[-2] == 'Y' or guess[2] == 'Da':
                start_game()
            else:
                quit()
        if guess[-2] in used_words:
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Try another letter. You used these letters: [', used_words, ']', Keys.ENTER)
            return hearing(max_tries, used_words, wrong_tries, random_word, hidden_word)
        elif guess[-2] not in used_words:
            used_words.append(guess[-2])
            used_words.append(',')
        if guess[-2] in random_word:
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Yes! The word contains this letter', Keys.ENTER)
            new = ''
            for i in range(len(random_word) - 1):
                if guess[-2] == random_word[i]:
                    new += guess[-2]
                else:
                    new += hidden_word[i]
            hidden_word = new
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(hidden_word, Keys.ENTER)
            return hearing(max_tries, used_words, wrong_tries, random_word, hidden_word)
        elif guess[-2] not in random_word:
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Oops! The wrong letter', Keys.ENTER)
            wrong_tries += 1
            return hearing(max_tries, used_words, wrong_tries, random_word, hidden_word)

def glavnoe(max_tries, used_words, wrong_tries, random_word, hidden_word):
    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]')))
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Hello. This is a hangman game!', Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('The word has ', len(random_word)-1, ' letters. Try to find out the word \n', hidden_word, Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]').click()
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

