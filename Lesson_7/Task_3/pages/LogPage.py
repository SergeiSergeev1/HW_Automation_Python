from selenium.webdriver.common.by import By

class LogPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_log(self, dataLog):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(dataLog['user-name'])
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(dataLog['password'])
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

   

    


