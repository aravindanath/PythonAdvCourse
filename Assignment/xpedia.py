from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='D:\\Drivers\\chromedriver.exe')
driver.get("https://www.expedia.co.in/")
driver.maximize_window()

flights = driver.find_element_by_xpath("//span[text()='Flights']")
flights.click()
driver.find_element_by_xpath("//span[text()='One-way']").click()
#From--------------

acts = ActionChains(driver)
flyfrom = driver.find_element_by_xpath("//label[contains(text(),'from')]")
fromInput = driver.find_element_by_xpath("//div[@class='uitk-field has-no-visible-label']/input")
acts.move_to_element(to_element=flyfrom).perform()
acts.click(on_element=flyfrom).perform()
time.sleep(3)
print(driver.title)
fromInput.send_keys("coi")
time.sleep(4)
driver.find_element_by_xpath("//strong[contains(text(),'Coimbatore (CJB - Coimbatore)')]").click()
acts.release(on_element=flyfrom).perform()
time.sleep(3)
# fromCities = driver.find_elements_by_xpath("//div[@class='uitk-dialog-content-wrapper'/div[1]/ul/li/div/div/span")
# for eachciti in fromCities:
#     print(eachciti).text
#     if eachciti.text == "Coimbatore (CJB - Coimbatore)":
#         eachciti.click()
#-----------To--------------------

flyTo = driver.find_element_by_xpath("//label[contains(text(),'to')]")
toInput = driver.find_element_by_xpath("//div[@class='uitk-field has-no-visible-label']/input[@placeholder='Where are you going to?']")
acts.move_to_element(to_element=flyTo).perform()
acts.click(on_element=flyTo).perform()
print(driver.title)
toInput.send_keys("hyd")
acts.release(on_element=flyTo).perform()
time.sleep(3)
driver.find_element_by_xpath("//span/strong[contains(text(), 'Hyderabad (HYD - Rajiv Gandhi Intl.)')]").click()
#---------Departing------------
# DeptInput= driver.find_element_by_xpath("//span[contains(text(),'Departing')]")
# acts.move_to_element(to_element=DeptInput).perform()
# acts.click(on_element=DeptInput).perform()
# monthPick = driver.find_element_by_id("//div[class='uitk-new-date-picker-desktop-months-container']/div/h2[contains(text(),'August 2020')]")
# acts.move_to_element(to_element=monthPick).perform()
# dateSelect=driver.find_element_by_xpath("//table[@class='uitk-new-date-picker-weeks']/tr[3]/td[4]")
# dateSelect.click()
# time.sleep(2)
#---------Search------------
Search = driver.find_element_by_xpath("//button[contains(text(),'Search')]")
Search.click()
time.sleep(10)

#-----Select Flight------
price= driver.find_element_by_xpath("//div[@class='uitk-col all-col-shrink']/div/div/div/span").text
print("Price is: "+price)
selFlight = driver.find_element_by_xpath("//div[@class='uitk-col all-col-shrink']/div/div[2]/button")
selFlight.click()
time.sleep(3)
driver.find_element_by_partial_link_text('No thanks').click()


