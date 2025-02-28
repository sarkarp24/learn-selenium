from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_option)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
title = driver.title
print(title)

driver.execute_script("window.scroll(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("end-of-page.png")
time.sleep(2)