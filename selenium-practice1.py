from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

#service_option = Service("/usr/bin/chromedriver")
#driver = webdriver.Chrome(service=service_option)

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
title = driver.title

checkbox = driver.find_elements(By.XPATH,"//label/input[@type='checkbox']")
#time.sleep(2)

for chk in checkbox:
    if chk.get_attribute("value") == "option2":
        chk.click()
        break

time.sleep(2)

enter_name = driver.find_element(By.NAME,"enter-name").send_keys("Prodyot")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.text
alert.accept()
#alert.dismiss()




