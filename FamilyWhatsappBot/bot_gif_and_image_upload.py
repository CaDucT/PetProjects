import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import sys
from gif_creator import make_gif
from PIL import Image
sys.setrecursionlimit(10000)
ser = Service(r"C:\webdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/nonse/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Profile 3')
driver = webdriver.Chrome(chrome_options=options, service=ser)
driver.maximize_window() # maximize browser's window
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

def hearing():
    a = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]').text
    time.sleep(2)
    b = a.strip().split()
    if b[-2] == 'Погода':
        aktau_weather()
    elif b[-2] == 'Море':
        caspiy_temp()
    else:
        time.sleep(5)
        hearing()

def caspiy_temp():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://travel.org.ua/water/aktau-temperatura-vody')
    element = driver.find_element(By.CSS_SELECTOR, 'body > center > div.x2 > div:nth-child(5) > div.x5 > div:nth-child(9) > div')
    location = element.location  # variable to define location of element choosed from screenshot
    size = element.size  # size variable of the element
    driver.save_screenshot('1.png')
    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\1.png')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]').click()
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]').click()
    pyautogui.moveTo(250, 50)
    time.sleep(1)
    pyautogui.write(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\1.png')
    time.sleep(1)
    pyautogui.press('enter')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')))
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
    time.sleep(2)
    hearing()

def aktau_weather():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://google.ru')
    driver.find_element(By.NAME, 'q').send_keys('погода актау', Keys.ENTER)
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    location = element.location  # variable to define location of element choosed from screenshot
    size = element.size  # size variable of the element
    driver.save_screenshot('1.png')
    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\1.png')

    driver.find_element(By.CSS_SELECTOR, '#wob_gsvg > text:nth-child(7)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\2.png')

    driver.find_element(By.CSS_SELECTOR,
                        '#wob_gsvg > text:nth-child(13)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\3.png')

    driver.find_element(By.CSS_SELECTOR,
                        '#wob_gsvg > text:nth-child(19)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\4.png')

    driver.find_element(By.CSS_SELECTOR,
                        '#wob_gsvg > text:nth-child(25)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\5.png')

    driver.find_element(By.CSS_SELECTOR,
                        '#wob_gsvg > text:nth-child(31)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\6.png')

    driver.find_element(By.CSS_SELECTOR,
                        '#wob_gsvg > text:nth-child(37)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\7.png')

    driver.find_element(By.CSS_SELECTOR,
                        '#wob_gsvg > text:nth-child(43)').click()  # choose the part of whole screenshot
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    driver.save_screenshot('1.png')  # save screenshot of whole screen

    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images\8.png')

    make_gif(r'C:\Users\nonse\PycharmProjects\PetProjects\google_images')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]').click()
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]').click()

    pyautogui.moveTo(250, 50)
    time.sleep(1)
    pyautogui.write(r'C:\Users\nonse\PycharmProjects\PetProjects\FamilyWhatsappBot\new.gif')
    time.sleep(1)
    pyautogui.press('enter')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')))
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
    time.sleep(2)
    hearing()


def glavnoe():
    #driver.get('http://google.ru')
    #driver.find_element(By.NAME, 'q').send_keys('курс кроны к тенге', Keys.ENTER)
    #curr = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

    #driver.get('http://google.ru')
    #driver.find_element(By.NAME, 'q').send_keys('погода актау', Keys.ENTER)
    #weather = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    #weather = weather + driver.find_element(By.XPATH, '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]').text

    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]')))
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]').click()
    time.sleep(2)

    #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Чатқа "Доллар" "Евро" "Погода" "Акш" "Крона" деп жаз', Keys.ENTER)
    #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Ақтауда ауа-райы қазір ', weather, Keys.ENTER)
    #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Курс кроны к тенге на сегодня ', curr, Keys.ENTER)
    #time.sleep(5)
    #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys('Бір цитата оқып ал, Чатқа "Цитата" деп жаз', Keys.ENTER)
    #driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    hearing()

if __name__ == '__main__':
    glavnoe()

