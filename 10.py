import requests
from time import sleep
from selenium import webdriver

for i in range(5):
    result = requests.get("https://github.com")
    if result.status_code != 200:
        print("GitHub is down")
        break
        sleep(1)
else:
    print("GitHub is Running")
