from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
press_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
for i in range(5):
    press_button.click()
    
added_elements = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print(len(added_elements))

sleep(2)
driver.quit()