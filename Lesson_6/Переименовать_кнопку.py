from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
button = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
button.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(blue_button)

driver.quit()