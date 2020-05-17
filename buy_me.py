import glob
import os
import random
import secrets
import string
import time
from os import path
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

firefox_driver = webdriver.Firefox(executable_path=r".\geckodriver.exe")


def get_a_random_pic():
    random_pic = glob.glob(str(os.path.join(os.environ["USERPROFILE"], r'Documents\*.png')))
    while not os.path.isfile(str(random_pic[0])):
        random_pic = input("Please enter a path to a png/jpg file: ")
    return random_pic[0]


def find_by_xpath_click(xpath):
    WebDriverWait(firefox_driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    firefox_driver.implicitly_wait(10)


def find_by_XPATH_enter_keys(xpath, text_input):
    WebDriverWait(firefox_driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(text_input)
    firefox_driver.implicitly_wait(10)


def find_element_by_link_text(xpath):
    WebDriverWait(firefox_driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, xpath))).click()
    firefox_driver.implicitly_wait(10)


random_email = ''.join(random.choice(string.ascii_letters) for _ in range(5))
random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
random_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10)) + "Ff1"


def buy_me():
    try:
        firefox_driver.get('http://buyme.co.il')
        firefox_driver.set_page_load_timeout(1)
        firefox_driver.maximize_window()
        # click on כניסה הרשמה
        find_by_xpath_click("//span[@class='seperator-link']")
        # click on להרשמה
        find_by_xpath_click("//span[@class='text-btn']")
        # Enter user info for sign up
        find_by_XPATH_enter_keys('//*[@class="ember-view ember-text-field"]', random_name)
        find_by_XPATH_enter_keys('//*[@type="email"]', random_email + '@gmail.com')
        find_by_XPATH_enter_keys('//*[@id="valPass"]', random_password)
        find_by_XPATH_enter_keys('//*[@placeholder="אימות סיסמה"]', random_password)
        find_by_xpath_click("//button[@type='submit']")
        time.sleep(1)
        # Select price point
        find_element_by_link_text("סכום")
        find_by_xpath_click("//li[@data-option-array-index='3']")
        # select area
        find_element_by_link_text("אזור")
        find_by_xpath_click("//li[@data-option-array-index='2']")
        # select category
        find_element_by_link_text("קטגוריה")
        find_by_xpath_click("//li[@data-option-array-index='5']")
        # click search
        find_by_xpath_click('//a[@class="card-item ember-view"]')
        # select business
        find_by_xpath_click("//a[@class='card-item ember-view']")
        # enter amount and click enter
        find_by_XPATH_enter_keys('//*[@placeholder="מה הסכום?"]', random.randint(100, 1000))
        find_by_xpath_click("//button[@type='submit']")
        # enter a name
        find_by_XPATH_enter_keys('//input[@data-parsley-required-message="מי הזוכה המאושר? יש להשלים את שם המקבל/ת"]',
                                 random_email)
        # upload a pic
        firefox_driver.find_element_by_xpath('//*[@name="fileUpload"]').send_keys(get_a_random_pic())
        # select event
        # firefox_driver.find_element_by_css_selector('#ember1504_chosen > a:nth-child(1)').click()
        find_element_by_link_text("לאיזה אירוע?")
        find_by_xpath_click("//li[@data-option-array-index='4']")
        # click email option
        find_by_xpath_click("//span[@class='icon icon-envelope']")
        # enter email address
        find_by_XPATH_enter_keys('//*[@type="email"]', random_email + '@gmail.com')
        # save email
        find_by_xpath_click("//button[@class='btn btn-theme btn-save']")
        # submit
        find_by_xpath_click("//button[@data-toggle='modal']")
    except BaseException as e:
        print(e)


buy_me()
