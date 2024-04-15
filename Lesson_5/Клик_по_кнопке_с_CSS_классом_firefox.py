from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

for i in range(3):
    driver.get("http://uitestingplayground.com/classattr")  
    blue_buton = driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()
    sleep(2)

driver.quit()