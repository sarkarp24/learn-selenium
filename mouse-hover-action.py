from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
title = driver.title
driver.maximize_window()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(2)
#top = driver.find_element(By.XPATH,"//a[@href='#top']").click()
action.context_click(driver.find_element(By.XPATH,"//a[@href='#top']")).perform()
time.sleep(2)





