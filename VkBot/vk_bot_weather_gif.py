from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyautogui
from PIL import Image
import time
from gif_creator import make_gif

ser = "C:\\webdrivers\\chromedriver.exe" #implement chromedriver path
driver = webdriver.Chrome(ser) #implement webdriver
driver.maximize_window() # maximize browser's window
driver.get('https://google.ru')
driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
spisok = ['биткоин', 'погода', 'курс']
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

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
    element = driver.find_element(By.XPATH, '//*[@id="wob_wc"]')  # choose the part of whole screenshot
    location = element.location  # variable to define location of element choosed from screenshot
    size = element.size  # size variable of the element
    driver.save_screenshot('1.png')  # save screenshot of whole screen

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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="im_editable46161369"]')))
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/div[2]/div/div/a').click()
    time.sleep(1)
    element_present = EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/div[2]/div/div/div/div/a[4]'))  # Example xpath
    WebDriverWait(driver, 10).until(element_present).click()  # This opens the windows file selector
    asd = EC.presence_of_element_located((By.XPATH, '//*[@id="docs_choose_upload_area"]/span'))
    WebDriverWait(driver, 10).until(asd).click()
    pyautogui.moveTo(250, 50)
    time.sleep(1)
    pyautogui.write(r'C:\Users\nonse\PycharmProjects\PetProjects\VkBot\google.gif')
    time.sleep(1)
    pyautogui.press('enter')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button/span[2]')))
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button/span[2]').click()
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