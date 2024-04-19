from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for i in range(3):
    driver.get("http://uitestingplayground.com/classattr")  
    blue_buton = driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()
    sleep(2)

driver.quit()