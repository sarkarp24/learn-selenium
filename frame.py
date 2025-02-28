from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/iframe")
title = driver.title
driver.implicitly_wait(5)

driver.switch_to.frame("mce_0_ifr")
frame_content = driver.find_element(By.XPATH,"//body[@id='tinymce']").text
print(frame_content)

driver.switch_to.default_content()
title = driver.find_element(By.XPATH,"//h3").text
print(title)


