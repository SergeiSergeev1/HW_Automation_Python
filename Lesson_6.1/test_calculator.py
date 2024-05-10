from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
    driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()
    wait = WebDriverWait(driver, 50)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'),'15'))
    result = driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
    assert result == '15'

    driver.quit()
