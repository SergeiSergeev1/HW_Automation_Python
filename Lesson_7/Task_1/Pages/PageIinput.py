from selenium.webdriver.common.by import By

class PageInput:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def data_entry(self, data):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(data['first-name'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(data['last-name'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(data['address'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(data['city'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(data['country'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(data['e-mail'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(data['phone'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(data['job-position'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(data['company'])
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()