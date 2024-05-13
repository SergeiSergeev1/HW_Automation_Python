from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ButtonPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def calculator_waits(self, term):
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(term)

    def push_the_button(self, keys_calculator):
        for val in keys_calculator:
            self.driver.find_element(By.XPATH, f'//span[text()="{val}"]').click()
            
        
    def closed_spiner(self) :
        term = self.driver.find_element(By.CSS_SELECTOR, '#delay').get_attribute('value')
        wait = WebDriverWait(self.driver, int(term) + 2)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[class="spinner-border"]')))


    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
        return(result)  
