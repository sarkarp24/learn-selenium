from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import tempfile
import time

options = Options()
user_data_dir = tempfile.mkdtemp() #Creates a temporary directory.
options.add_argument(f"--user-data-dir={user_data_dir}")

service = Service()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

driver.get("http://192.168.4.80:8082/contact.html")
driver.maximize_window()
print(driver.title)

name = driver.find_element(By.XPATH,"//input[@name='your_name']").send_keys("Prodyot Sarkar")
phone = driver.find_element(By.XPATH,"//input[@name='phone_number']").send_keys("1234567890")
email = driver.find_element(By.XPATH,"//input[@name='email_address']").send_keys("psarkar@test.com")
email = driver.find_element(By.XPATH,"//input[@name='your_message']").send_keys("psarkar@test.com")
driver.find_element(By.XPATH,"//button[@id='my-button']").click()
response = driver.find_element(By.ID,"response").text
print(response)

try:
    assert response == 'Message Sent'
    print("Testing Successfull!!!")
except AssertionError as e:
    print("Assertion error!!!")

driver.quit()
import shutil
shutil.rmtree(user_data_dir) #removes the temp directory.