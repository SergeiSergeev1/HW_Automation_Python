from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
serch_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
serch_input.send_keys("1000")
sleep(1)
serch_input.clear()
sleep(1)
serch_input.send_keys("999")
sleep(1)
driver.quit()