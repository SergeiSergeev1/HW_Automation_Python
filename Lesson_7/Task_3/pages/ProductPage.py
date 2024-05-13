from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        #self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def choice_of_goods(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()