from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

# from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.find_element_by_xpath("//input[starts-with(@id,'user')]").send_keys("arvind")
time.sleep(2)
driver.quit()