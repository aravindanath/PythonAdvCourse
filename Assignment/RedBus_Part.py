from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

import time


driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.redbus.in")
driver.find_element_by_css_selector("#src").send_keys("Bang")
time.sleep(3)
src = driver.find_elements_by_xpath("//ul[@class='autoFill']/li")

print("Total no of pickup", len(src))

