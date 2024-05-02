from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_buy():
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    waiter = WebDriverWait(driver, 10)
    waiter.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
    waiter.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    waiter.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ivan")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Ivanov")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    waiter.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
    Total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    print(Total)
    assert Total == "Total: $58.29"
    driver.find_element(By.CSS_SELECTOR, "#finish").click()


    driver.quit()


