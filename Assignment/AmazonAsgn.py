from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
driver.get("http://www.amazon.in")
driver.maximize_window()
searchBox = driver.find_element_by_id('twotabsearchtextbox')
searchBox.send_keys("men's watch")
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(5)
watchType = driver.find_element_by_xpath("//li[@aria-label='Analogue']").click()
time.sleep(5)
# discount = driver.find_element_by_xpath("//span[contains(text(),'25% Off or more')]").click()
watchPrice = driver.find_element_by_xpath("//div[@data-index='4']//span[@class='a-offscreen']").text
#print(watchPrice)

