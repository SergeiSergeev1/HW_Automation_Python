from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ButtonPage import ButtonPage


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pushbutton = ButtonPage(browser)
    pushbutton.calculator_waits('45')
    pushbutton.push_the_button('C7+8=')
    pushbutton.closed_spiner()
    as_is = pushbutton.get_result()
    assert as_is == '15'

    browser.quit()


    

