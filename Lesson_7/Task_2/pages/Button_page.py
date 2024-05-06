from selenium.webdriver.common.by import By

class Button_page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def push_the_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
        self.driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

