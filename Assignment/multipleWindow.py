from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import  time

driver = Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get("https://www.tripadvisor.in/")
print(driver.title)

driver.find_element_by_xpath("(//input[@type='search' and @name='q'])[2]").send_keys("club mahindra",Keys.ENTER)
parent = driver.current_window_handle
print("Parent ", parent)
time.sleep(3)
review =driver.find_element_by_xpath("(//a[@class='review_count'])[2]")
act = ActionChains(driver)
act.click(review).perform()

wins = driver.window_handles
for w in wins:
    driver.switch_to.window(w)
    print(w)

print(driver.title)

time.sleep(3)
rw2 = driver.find_element_by_xpath("//a[text()='Write a review']")
act = ActionChains(driver)
act.click(rw2).perform()
time.sleep(1)
wins = driver.window_handles
for w in wins:
    driver.switch_to.window(w)
    print(w)

print(driver.title)
time.sleep(2)
driver.switch_to.window(parent)

time.sleep(2)
print(driver.title)
driver.quit()




