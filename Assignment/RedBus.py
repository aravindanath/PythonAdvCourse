from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

# from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())
# driver = Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
driver.get("https://www.redbus.in/")
driver.maximize_window()
FCity = driver.find_element_by_id("src").send_keys("Ba")
time.sleep(3)
Fromlist = driver.find_elements_by_xpath("//ul[@class='autoFill']")
FcityList = []
for city in Fromlist:
    print(city.text)
    if city.text == "Majestic, Bangalore":
        city.click()
    selectFromcity = city.text
    match1= re.findall("Bax*",selectFromcity)
    if match1:
        FcityList.append(selectFromcity.replace(",", " "))

time.sleep(5)

# print("---------")
# for i in FcityList:
#     print(i)
# time.sleep(4)
# driver.find_element_by_xpath("//li[contains(text(),'Madiwala, Bangalore')]").click()
# print("-----")
# driver.find_element_by_id("dest").send_keys("Hyd")
# ToList = driver.find_elements_by_xpath("//ul[@class='autoFill']/li")
# time.sleep(3)
# #xpath("//div[@class='fl search-box']/div/ul[@class='autoFill']")
# for toCity in ToList:
#     # x=1
#     # destn1 = driver.find_elements_by_xpath("ToList/li["+"x"+"]")
#     print(toCity.text)
#     # x = x+1
#     # selectToCity = toCity.text
#     # if toCity == "Secunderabad, Hyderabad":
#     #     toCity.click()
# DestList = ["Kukatpally", "Kondapur", "Secunderabad", "Malakpet"]
# # for x,y in zip(FcityList, DestList):
# #     print(x,"********", y)
# mapped = zip(FcityList, DestList)
# mapped = tuple(mapped)
# print(mapped)
driver.close()
#
#
