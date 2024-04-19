from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")
serch_log = driver.find_element(By.CSS_SELECTOR, '#username')
serch_log.send_keys('tomsmith')
serch_pass = driver.find_element(By.CSS_SELECTOR, '#password')
serch_pass.send_keys('SuperSecretPassword!')
sleep(1)
button_login = driver.find_element(By.CSS_SELECTOR, '.radius').click()
sleep(2)
driver.quit()