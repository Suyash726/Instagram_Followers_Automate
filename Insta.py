from selenium import webdriver
from time import  sleep

from Secret import number,password

class Insta_Bot:
    def __init__(self):
        self.driver=webdriver.Chrome("F:\\chromedriver.exe")

    def login(self):
        self.driver.get('https://instagram.com')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(number)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(5)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a/img').click()
        
    def get_followers(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        

i = Insta_Bot()
i.login()
i.get_followers()