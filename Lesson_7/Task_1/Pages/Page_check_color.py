from selenium.webdriver.common.by import By

class Page_check_color:

    def __init__(self, driwer):
        self.driver = driwer

    def check_color_zip_code(self):
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        return (zip_code_color)

    def check_color_other_field(self):
        other_fields = ['#first-name, #last-name, #address, #city, #country, #e-mail, #phone, #job-position, #company']
        for field in other_fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property('background-color')
            return(field_color)
        
        