from selenium.webdriver.common.by import By

class Page_input:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def data_entry(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()