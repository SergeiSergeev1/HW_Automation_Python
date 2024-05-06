from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Page_Iinput import Page_input
from Pages.Page_check_color import Page_check_color


def test_input_fields():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pageinput = Page_input(browser)
    pageinput.data_entry()
    pagecheck = Page_check_color(browser)
    pagecheck.check_color_zip_code()
    zip_code = pagecheck.check_color_zip_code()
    assert zip_code ==  'rgba(248, 215, 218, 1)'
    pagecheck.check_color_other_field()
    other_fields = pagecheck.check_color_other_field()
    assert other_fields == 'rgba(209, 231, 221, 1)'

    browser.quit()
 
    

   

