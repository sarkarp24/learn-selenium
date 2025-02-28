from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# ID, XPATH, Classname, CSSSelector, Name, LinkText

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
title = driver.title
driver.implicitly_wait(5)

search_products = driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

#add_to_cart = driver.find_elements(By.XPATH,"//div[@class='products']/div/div[@class='product-action']")
add_to_cart = driver.find_elements(By.XPATH,"//div[@class='products']/div")
#print(add_to_cart)
for cart in add_to_cart:
    #print(cart.find_element(By.CSS_SELECTOR,".product-name").text)
    print(cart.find_element(By.XPATH,"h4").text)
    cart.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()
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

#explicit wait

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promoApplied = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

print(promoApplied)
assert promoApplied == 'Code applied ..!'

time.sleep(2)

each_totals = driver.find_elements(By.XPATH,"//tbody/tr/td[5]/p[@class='amount']")
tbl_total = 0
for each_total in each_totals:
    assert int(each_total.text)
    tbl_total = tbl_total + int(each_total.text)

tot_amt = driver.find_element(By.CSS_SELECTOR,".totAmt")
print('Table Total:{}'.format(tbl_total))
print('Total Amount:{}'.format(int(tot_amt.text)))
assert tbl_total == int(tot_amt.text)


#alert = driver.switch_to.alert
#alert.text
#alert.accept()
#alert.dismiss()
