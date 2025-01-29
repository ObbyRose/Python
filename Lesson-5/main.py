from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def test_product_search():
    driver = webdriver.Chrome()
    base_url = "https://atid.store/product-category/men/"

    driver.get(base_url)
    driver.maximize_window()
    search_box = driver.find_element(By.ID , "wc-block-search__input-1").send_keys('ATID Blue Shoes')
    click_search = driver.find_element(By.CLASS_NAME, "wc-block-product-search__button").click()
    if not(driver.current_url == base_url):
        print("Test Passed")
    else:
        print("Test Failed")
    product_title = driver.find_element(By.XPATH, "//h1[normalize-space()='ATID Blue Shoes']")
    print(product_title.text)
    product_price = driver.find_element(By.XPATH, "//div[@class='summary entry-summary']//ins//bdi[1]")
    print(product_price.text.replace('₪', ''))
    time.sleep(5)

# test_product_search()

def test_title():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.maximize_window()
    main_string = driver.find_element(By.XPATH , "//h1[@class='elementor-heading-title elementor-size-default']").text
    print(main_string)
    if "ATID" in main_string:
        print("Test Passed")
    else:
        print("Test Failed")
    time.sleep(5)

# test_title()