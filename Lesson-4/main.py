import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path="./chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# driver.maximize_window()
# print(driver.title)
# time.sleep(5)

# driver.get("https://atid.store")
# driver.get("https://www.google.com")
# driver.back()
# driver.forward()
# driver.refresh()
# driver.quit()
# time.sleep(10)

driver.get("https://atid.store")
shop_button = driver.find_element(By.XPATH, "//a[@href='https://atid.store/store/']//span[@class='elementor-button-content-wrapper']//span[@class='elementor-button-text'][normalize-space()='Shop Now']")

time.sleep(10)