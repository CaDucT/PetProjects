from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
ser = "C:\\webdrivers\\chromedriver.exe"
driver = webdriver.Chrome(ser)
driver.maximize_window() # maximize browser's window

driver.get('http://google.ru')
driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
driver.find_element(By.NAME, 'q').send_keys('курс кроны к тенге', Keys.ENTER)
curr = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
driver.find_element(By.NAME, 'q').clear()
driver.find_element(By.NAME, 'q').send_keys('погода в праге', Keys.ENTER)
weather = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
weather = weather + driver.find_element(By.XPATH, '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]').text
driver.find_element(By.NAME, 'q').clear()
driver.find_element(By.NAME, 'q').send_keys('биткоин доллар', Keys.ENTER)
btc = driver.find_element(By.XPATH, '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]').text


driver.get('https://vk.com')

driver.find_element(By.XPATH, '//*[@id="index_email"]').send_keys('+77753054795')
driver.find_element(By.XPATH, '//*[@id="index_login"]/div/form/button[1]/span').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input')))
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input').send_keys('qwerty4444')
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/button/span[1]/span').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="l_fr"]')))
driver.find_element(By.XPATH, '//*[@id="l_fr"]').click()#click friends
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="friends_user_row46161369"]/div[3]/div[4]/a')))
driver.find_element(By.XPATH, '//*[@id="friends_user_row46161369"]/div[3]/div[4]/a').click()#find friend and click text message
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a')))
driver.find_element(By.XPATH, '//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()#click redirect to private messages

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="im_editable46161369"]')))
driver.find_element(By.XPATH, '//*[@id="im_editable46161369"]').send_keys('Курс кроны к тенге на сегодня ', curr, Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="im_editable46161369"]').send_keys('Погода сейчас ', weather, Keys.ENTER)#enter message"""
driver.find_element(By.XPATH, '//*[@id="im_editable46161369"]').send_keys('Курс биткоина ', btc, Keys.ENTER)
time.sleep(2)
driver.quit()