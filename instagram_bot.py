import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from username1 import usernamem, passwordm, musteri

resul = webdriver.Chrome()

url = 'https://www.instagram.com/'
resul.get(url)
time.sleep(3)
resul.find_element(By.NAME, 'username').send_keys(usernamem)
time.sleep(3)
resul.find_element(By.NAME,'password').send_keys(passwordm)

ActionChains(resul) \
    .key_down(Keys.ENTER) \
    .send_keys("abc") \
    .perform()
time.sleep(5)
url2 = 'https://www.instagram.com/' + musteri
resul.get(url2)
time.sleep(5)

elm = resul.find_element(By.CLASS_NAME,'_acas')
elm.click()


time.sleep(20)
