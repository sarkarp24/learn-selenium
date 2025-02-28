from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/windows")
title = driver.title
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT,"Click Here").click()
windowList = driver.window_handles
driver.switch_to.window(windowList[1])
time.sleep(2)

print(driver.find_element(By.XPATH,"//h3[text()='New Window']").text)

driver.switch_to.window(windowList[0])
print(driver.find_element(By.XPATH,"//h3[text()='Opening a new window']").text)
