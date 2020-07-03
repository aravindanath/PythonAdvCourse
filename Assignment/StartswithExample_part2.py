from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

# from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.linkedin.com")
header = driver.find_element_by_xpath("//*[starts-with(@class,'hero__h')]").text
print("Header: "+ header)
assert header == "Welcome to your professional community"
time.sleep(2)
driver.quit()