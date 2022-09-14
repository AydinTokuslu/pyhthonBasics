from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username,password):
        self.browserProfile=webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en, en_US'})
        self.browser=webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput=self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        # passwordInput=self.browser.find_element_by_xpath("")

        usernameInput.send_keys(self.username)



twitter=Twitter(username,password)
# login
twitter.signIn()
