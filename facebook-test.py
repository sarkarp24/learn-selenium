from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
driver.maximize_window()
driver.implicitly_wait(5000)
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
text_box.send_keys("Selenium")

password = driver.find_element(by=By.NAME, value="my-password")
password.send_keys("selenium")
time.sleep(1)

text_area = driver.find_element(by=By.NAME, value="my-textarea")
text_area.send_keys("Hi! How Are you? I am doing good!")
time.sleep(1)


dropdown_select = Select(driver.find_element(By.XPATH,"//select[@name='my-select']"))
dropdown_select.select_by_index(2)
dropdown_select.select_by_value("3")
dropdown_select.select_by_index(1)
time.sleep(1)

dropdown_input = driver.find_elements(By.XPATH,"//label/datalist/option")
for opt in dropdown_input:
    #print(opt)
    #print(opt.get_attribute("value"))
    if opt.get_attribute("value") == "New York":
        city = opt.get_attribute("value")
        print(city)
        select_element = driver.find_element(By.XPATH,"//input[@name='my-datalist']")
        select_element.send_keys(city)
        select_element.click()
        break
'''

dropdown_input = driver.find_element(By.XPATH,"//input[@name='my-datalist']")
dropdown_input.send_keys("Seattle")
time.sleep(1)
dropdown_input.click()

'''

checked_checkbox = driver.find_element(By.XPATH,"//input[@id='my-check-1']")
checked_checkbox.click()
time.sleep(1)

default_checkbox = driver.find_element(By.CSS_SELECTOR,"input[id='my-check-2']")
default_checkbox.click()
time.sleep(1)

check_radio = driver.find_element(By.XPATH,"//input[@id='my-radio-1']")
check_radio.click()
time.sleep(1)

default_radio = driver.find_element(By.CSS_SELECTOR,"input[id='my-radio-2']")
default_radio.click()
time.sleep(1)


submit_button.click()
message = driver.find_element(By.ID, "message")
text = message.text
#driver.implicitly_wait(10000)
time.sleep(1)

print(text)
print("----")
driver.quit()