import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

def open_chrome_chrome(url, element_to_find, skip):
    driver = webdriver.Chrome(executable_path="C:\windows\system32\chromedriver.exe")
    driver.get(url)
    if skip is False:
        title = driver.title
        driver.refresh()
        if title in driver.title:
            print("The title is the same")
        else:
            print("The title is Not the same")
    try:
        element = driver.find_element_by_id(element_to_find)
        driver.close()
        return element
    except BaseException as e:
        print(e)


def open_firefox_browser(url, element_to_find):
    firefox_driver = webdriver.Firefox(executable_path="C:\windows\system32\geckodriver.exe")
    firefox_driver.get(url)
    # compare random element
    try:
        temp_element = firefox_driver.find_element_by_id(element_to_find)
        return temp_element
    except BaseException as e:
        print(e)
    # google translate text input
    try:
        element = firefox_driver.find_element_by_id(element_to_find)
        return element
    except BaseException as e:
        print(e)


# YouTube search
def browser_plus_click(url, element_to_find, text_input):
    firefox_driver = webdriver.Firefox(executable_path="C:\windows\system32\geckodriver.exe")
    firefox_driver.get(url)
    try:
        WebDriverWait(firefox_driver, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, element_to_find))).send_keys(text_input)
        # firefox_driver.find_element_by_css_selector(button_element).click()
        firefox_driver.find_element_by_tag_name(element_to_find).send_keys(Keys.ENTER)
    except BaseException as e:
        print(e)


# open Facebook and login
def open_facebook(url):
    user = input("Please Enter your username")
    password = input("Please enter your password")
    driver = webdriver.Chrome(executable_path="C:\windows\system32\chromedriver.exe")
    driver.get(url)

    driver.find_element_by_id('email').send_keys(user)
    driver.find_element_by_id('pass').send_keys(password)

    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()


# get and delete all browser cookies
def get_cookies(url):
    driver = webdriver.Chrome(executable_path="C:\windows\system32\chromedriver.exe")
    driver.get(url)
    print(driver.get_cookies())
    driver.delete_all_cookies()
    print('All cookies have been deleted' + str(driver.get_cookies()))


# compare elements
chrome = open_chrome_chrome('http://www.walla.co.il', "adSlot-0", skip=True)
firefox = open_firefox_browser('http://www.walla.co.il', 'adSlot-0')
if chrome == firefox:
    print("The elements are the same")
else:
    print("The elements are different")

# open browser get title and refresh, check if still the same
open_chrome_chrome('http://www.walla.co.il', "adSlot-0", skip=False)
#
# Google Translate
open_firefox_browser('https://translate.google.com/', 'source').send_keys('ניסיון')
#
# YouTube search
browser_plus_click('https://youtube.com/', "input", 'Random song')

# open GitHub and search
browser_plus_click('http://github.com', 'input', 'selenium')

# open facebook and login
open_facebook('https://www.facebook.com/')

# Delete cookies
get_cookies('https://zoom.us/')
