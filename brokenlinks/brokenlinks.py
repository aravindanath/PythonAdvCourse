from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import requests

driver = Chrome(ChromeDriverManager().install())
driver.get("http://www.deadlinkcity.com/")
links = driver.find_elements_by_tag_name("a")
r =  200
for link in links:
    r = requests.head(link.get_attribute("href"))
    if r.status_code >=400:
        print(str(link.get_attribute('href')) + " is broken link ")
    elif r.status_code ==200:
        print(str(link.get_attribute('href')) + " is  available.")
