from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Button_page import Button_page
from pages.Wait_result_page import Wait_result


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pushbutton = Button_page(browser)
    pushbutton.push_the_button()
    waitresult = Wait_result(browser)
    waitresult.closed_spiner()
    waitresult.get_result()
    as_is = waitresult.get_result()
    assert as_is == '15'

    browser.quit()


    

