from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LogPage import LogPage
from pages.ProductPage import ProductPage
from pages.OrderPage import OrderPage




def test_shoppin_site():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    logpage = LogPage(browser)
    logpage.input_log()
    productpage = ProductPage(browser)
    productpage.choice_of_goods()
    orderpage = OrderPage(browser)
    orderpage.confirm()
    orderpage.input_fields()
    as_it = orderpage.get_total_price()
    assert as_it == "Total: $58.29"

    browser.quit()




   


    


  
