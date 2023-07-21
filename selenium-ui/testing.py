from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

unameGet = driver.find_element(By.ID, "login_credentials").text
passGet = driver.find_element(By.CLASS_NAME, "login_password").text

username = unameGet.split('\n')[1]
password = passGet.split('\n')[1]

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

getPrice = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
priceBgpck = getPrice.text

driver.find_element(By.XPATH, ("/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")).click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

price2 = driver.find_element(By.XPATH, ("/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div")).text

assert priceBgpck == price2


driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Testing")
driver.find_element(By.ID, "last-name").send_keys("selenium")
driver.find_element(By.ID, "postal-code").send_keys("10000")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()

assert "Complete!" in driver.find_element(By.CLASS_NAME, "title").text

print('Test passed')

time.sleep(3)

driver.quit()