from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

url="http://github.com"

driver.get(url)
driver.maximize_window()

searchInput=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
driver.close()