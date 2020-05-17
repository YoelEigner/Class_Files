from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome()

my_driver.get("file://C:/Users/joele/Downloads/tip_calc/index.html")
bill_amt = my_driver.find_element_by_id("billamt")
bill_amt.send_keys("100")

selection = my_driver.find_element_by_id("serviceQual")
selection.click()

select = my_driver.find_element_by_id("option", value=0.3)
select.clear()

ppl = my_driver.find_element_by_id("peopleamt")
ppl.send_keys("5")
