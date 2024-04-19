from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(1)
    click_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    sleep(1)
   

driver.quit()






