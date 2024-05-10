from selenium.webdriver.common.by import By

class PageCheckColor:

    def __init__(self, driver):
        self.driver = driver

    def check_red_color(self):
        red_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property('background-color')
        return (red_color)

  
    
    def check_green_color(self):
        green_colors = ['#first-name', '#last-name', '#address', '#city,#country', '#e-mail', '#phone', '#job-position', '#company']
        green_color_values = []
        for field in green_colors:
            green_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property('background-color')
            green_color_values.append(green_color)
        return green_color_values
        
        
        