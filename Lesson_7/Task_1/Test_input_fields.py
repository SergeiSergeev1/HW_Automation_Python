from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageIinput import PageInput
from Pages.PageCheckColor import PageCheckColor
from time import sleep


data = {
    'first-name': 'Иван',
    'last-name': 'Петров',
    'address': 'Ленина, 55-3',
    'city': 'Москва',
    'country': 'Россия',
    'e-mail': 'test@skypro.com',
    'phone': '+7985899998787',
    'job-position': 'QA',
    'company': 'SkyPro'
}

def test_input_fields():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pageinput = PageInput(browser)
    pageinput.data_entry(data)
    pagecheck = PageCheckColor(browser)
    zip_code = pagecheck.check_red_color()
    assert zip_code ==  'rgba(248, 215, 218, 1)'
    other_fields = pagecheck.check_green_color()
    for field_color in other_fields:
        assert field_color == 'rgba(209, 231, 221, 1)'
 
    browser.quit()
 
    

   

