from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
press_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
for i in range(5):
    press_button.click()
    
added_elements = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print(len(added_elements))

sleep(2)
driver.quit()