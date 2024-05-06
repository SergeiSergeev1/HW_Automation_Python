from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait_result:

    def __init__(self, driver):
        self.driver = driver

    def closed_spiner(self) :
        wait = WebDriverWait(self.driver, 47)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[class="spinner-border"]')))

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
        return(result)