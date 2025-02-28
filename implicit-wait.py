from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
title = driver.title
driver.implicitly_wait(5)

search_products = driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

add_to_cart = driver.find_elements(By.XPATH,"//div[@class='products']/div/div[@class='product-action']")
for cart in add_to_cart:
    print(cart.text)
    cart.click()
#time.sleep(2)

click_cart = driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']")
click_cart.click()
#time.sleep(2)
proceed_chkout = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
proceed_chkout.click()

#time.sleep(2)

print(driver.current_url)

promoCode = driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
promoBtn = driver.find_element(By.CSS_SELECTOR,".promoBtn")
promoBtn.click()

#time.sleep(8)

promoApplied = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

print(promoApplied)
assert promoApplied == 'Code applied ..!'

time.sleep(2)


