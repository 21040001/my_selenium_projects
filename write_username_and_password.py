from selenium import webdriver
from selenium.webdriver.common.by import By
from username1 import usernamem1, passwordm1 # bu ishlashi uchun ozingiz username1 nomli bir fayl ochib username1='__' password1='__' bu shakilda foydalanuvchi nomingiz va parolingizni kirishingiz kerak.
import  time


class Github:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.user = usernamem1
        self.pas = passwordm1

    def kir(self):
        self.browser.get('https://www.youtube.com/channel/UCtxypCLZEd8v3AoUu-xZS4w')
        time.sleep(2)

        self.browser.find_element(By.XPATH,'//*[@id="OtherUsername"]').send_keys(self.user)


        self.browser.find_element(By.XPATH,'//*[@id="OtherPassword"]').send_keys(self.pas)
       #self.browser.find_element(By.XPATH, '//*[@id="rememberusername"]').click()
        time.sleep(3)
        self.browser.find_element(By.XPATH,'//*[@id="btnSend"]').click()
        time.sleep(5)


github = Github()
github.kir()
