from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

import time


driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.redbus.in/")

driver.find_element_by_id("src").send_keys("Bang")

src = driver.find_elements_by_xpath("//ul[@class='autoFill']/li")

print("Total no of pickup point:", len(src))

for s in src:
    print(s.text)
    if s.text=="White Field, Bangalore":
        s.click()
        break


time.sleep(4)

driver.find_element_by_id("dest").send_keys("hyd")
dest =driver.find_elements_by_xpath("//ul[@class='autoFill']/li")
print("Total no of drop point:", len(dest))

for d in dest:
    if d.text=="Uppal, Hyderabad":
        d.click()
        break


time.sleep(5)



driver.find_element_by_css_selector(".icon-onward-calendar").click()
time.sleep(1)

fromDate = driver.find_elements_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td")

for f in fromDate:
    if f.text != "July 2020":
        driver.find_element_by_xpath("//button[text()='>']").click()
        break

time.sleep(3)

fromDate = driver.find_elements_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td")

for f in fromDate:
    if f.text == "29":
        f.click()
        break



time.sleep(5)
driver.quit()




