from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PIL import Image
import time
import os

ser = "C:\\webdrivers\\chromedriver.exe"
driver = webdriver.Chrome(ser)
driver.maximize_window() # maximize browser's window
driver.get('https://google.ru')
driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img")
location = element.location
size = element.size
driver.save_screenshot("pageImage.png")

# crop image
x = location['x']
y = location['y']
width = location['x']+size['width']
height = location['y']+size['height']
im = Image.open('pageImage.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('element.png')
spisok = ['биткоин', 'погода', 'курс']

def listen_to():
    while True:
        time.sleep(1)
        guess = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]').text
        guess = guess.strip().split()
        if guess[-1].lower() in spisok:
            break
    if guess[-1].lower() in spisok:
        if guess[-1].lower() == 'биткоин':
            btc()
        elif guess[-1].lower() == 'погода':
            weather()
        elif guess[-1].lower() == 'курс':
            curr()

def weather():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').clear()
    driver.find_element(By.NAME, 'q').send_keys('погода в праге', Keys.ENTER)
    weather = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    weather = weather + driver.find_element(By.XPATH, '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]').text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="im_editable46161369"]')))
    driver.find_element(By.XPATH, '//*[@id="im_editable46161369"]').send_keys('Погода сейчас ', weather, Keys.ENTER)
    time.sleep(1)
    listen_to()

def btc():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').clear()
    driver.find_element(By.NAME, 'q').send_keys('биткоин доллар', Keys.ENTER)
    btc = driver.find_element(By.XPATH, '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]').text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="im_editable46161369"]')))
    driver.find_element(By.XPATH, '//*[@id="im_editable46161369"]').send_keys('Курс биткоина ', btc, Keys.ENTER)
    time.sleep(1)
    listen_to()
def curr():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').clear()
    driver.find_element(By.NAME, 'q').send_keys('курс кроны к тенге', Keys.ENTER)
    curr = driver.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="im_editable46161369"]')))
    driver.find_element(By.XPATH, '//*[@id="im_editable46161369"]').send_keys('Курс кроны к тенге на сегодня ', curr, Keys.ENTER)
    time.sleep(1)
    listen_to()

def vk_sign():

    driver.get('https://vk.com')
    driver.find_element(By.XPATH, '//*[@id="index_email"]').send_keys('+77753054795')
    driver.find_element(By.XPATH, '//*[@id="index_login"]/div/form/button[1]/span').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input').send_keys('qwerty4444')
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/button/span[1]/span').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="l_fr"]')))
    driver.find_element(By.XPATH, '//*[@id="l_fr"]').click()  # click friends
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="friends_user_row46161369"]/div[3]/div[4]/a')))
    driver.find_element(By.XPATH,
                        '//*[@id="friends_user_row46161369"]/div[3]/div[4]/a').click()  # find friend and click text message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a')))
    driver.find_element(By.XPATH,
                        '//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()  # click redirect to private messages

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="im_editable46161369"]')))
    listen_to()

vk_sign()