from selenium.webdriver.common.by import By

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def confirm(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def input_fields(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ivan")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Ivanov")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total_price(self):
        Total = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return Total
    
    def close_site(self):
        self.driver.find_element(By.CSS_SELECTOR, "#finish").click()

    
        
    
    
        
   


    