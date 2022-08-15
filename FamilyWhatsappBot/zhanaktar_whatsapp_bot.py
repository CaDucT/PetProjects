from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import sys

sys.setrecursionlimit(10000)
ser = Service(r"C:\webdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/nonse/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Profile 3')
driver = webdriver.Chrome(chrome_options=options, service=ser)
driver.maximize_window() # maximize browser's window

def hearing():
    a = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]').text
    time.sleep(2)
    b = a.strip().split()
    if b[-2] == 'Доллар':
        usdkzt()
    elif b[-2] == 'Акш':
        aqsuqur_weather()
    elif b[-2] == 'Погода':
        aktau_weather()
    elif b[-2] == 'Евро':
        kurs_evro()
    elif b[-2] == 'Крона':
        kurs_krona()
    elif b[-2] == 'Цитата':
        citaty()
    else:
        time.sleep(5)
        hearing()

def aqsuqur_weather():
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('погода акшукур', Keys.ENTER)
    weather = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    weather = weather + driver.find_element(By.XPATH, '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]').text
    driver.get('https://web.whatsapp.com/')
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Погода в Акшукур сейчас ', weather, Keys.ENTER)
    hearing()
def usdkzt():
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('курс доллара к тенге', Keys.ENTER)
    usdt = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Курс доллара к тенге на сегодня ', usdt, Keys.ENTER)
    time.sleep(2)
    hearing()

def aktau_weather():
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('погода актау', Keys.ENTER)
    weather = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    weather = weather + driver.find_element(By.XPATH, '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]').text
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Погода в Актау сейчас ', weather, Keys.ENTER)
    hearing()

def kurs_evro():
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('курс евро к тенге', Keys.ENTER)
    curr = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Курс Евро к тенге на сегодня ', curr, Keys.ENTER)
    hearing()

def kurs_krona():
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('курс кроны к тенге', Keys.ENTER)
    curr = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Курс кроны к тенге на сегодня ', curr, Keys.ENTER)
    hearing()

def citaty():
    driver.get('https://finewords.ru/sluchajnye-citaty')
    driver.find_element(By.XPATH, '//*[@id="ischoodna"]').click()
    c = driver.find_element(By.XPATH, '//*[@id="sluchaino"]').text
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(c, Keys.ENTER)
    time.sleep(2)
    hearing()

def glavnoe():
    #driver.get('http://google.ru')
    #driver.find_element(By.NAME, 'q').send_keys('курс кроны к тенге', Keys.ENTER)
    #curr = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('погода актау', Keys.ENTER)
    weather = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    weather = weather + driver.find_element(By.XPATH, '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]').text

    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Чатқа "Доллар" "Евро" "Погода" "Акш" "Крона" деп жаз', Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Ақтауда ауа-райы қазір ', weather, Keys.ENTER)
    #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Курс кроны к тенге на сегодня ', curr, Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Бір цитата оқып ал, Чатқа "Цитата" деп жаз', Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    hearing()

if __name__ == '__main__':
    glavnoe()

