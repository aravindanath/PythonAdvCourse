from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Assignment import Generic as gs

import time

# driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
driver = Chrome(ChromeDriverManager().install())
driver.get("http://www.amazon.in")
driver.maximize_window()
searchBox = driver.find_element_by_id('twotabsearchtextbox')
searchBox.send_keys("men's watch")
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(5)

mov = driver.find_element_by_xpath("(//span[contains(text(),'Watch Movement') or contains(text(),'Movement')])[1]")
print(mov.text)

driver.execute_script("arguments[0].scrollIntoView();",mov)
driver.refresh()


time.sleep(5)
leather= driver.find_element_by_xpath("//span[text()='Leather']")
gs.actionClick(driver,leather)

time.sleep(5)
products = driver.find_elements_by_css_selector(".s-main-slot.s-result-list.s-search-results.sg-row>div>div")
print("Total no of products",len(products))
products[5].click()



