import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


# get and delete all browser cookies
def get_cookies(url):
    driver = webdriver.Chrome(executable_path="C:\windows\system32\chromedriver.exe")
    driver.get(url)
    print(driver.get_cookies())
    driver.delete_all_cookies()
    print('All cookies have been deleted' + str(driver.get_cookies()))


# Delete cookies
# get_cookies('https://zoom.us/')
