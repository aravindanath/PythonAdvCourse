#how to print class attribute value,
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import pytest

#def launchBrowser():

# driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
Url = "https://www.mysmartprice.com/mobile/apple-iphone-xir-msp15688"

driver.get(Url)
driver.maximize_window()
mobileList = driver.find_elements_by_xpath("//div[@class='prc-box prc-tbl--fullcards']/div")
mobilePrice = []

for eachMobile in mobileList:
   # name = eachMobile.
    #print(name)
    price = eachMobile.find_element_by_xpath("div/div[2]").text

    print(price)
    mobilePrice.append(str(price).replace('₹', "" ).replace(',', ""))

print("list before sort")
print(mobilePrice)
print("list after sort")
mobilePrice.sort()
print(mobilePrice)

parentWin = driver.current_window_handle

amazonLnk = driver.find_element_by_xpath("//div[@class='prc-box prc-tbl--fullcards']/div/div/div[3]/a")
amazonLnk.click()
childWindow= driver.window_handles
for eachwin in childWindow:
    driver.switch_to.window(eachwin)

# home_win = driver.window_handles[0]
# amazon_win = driver.window_handles[1]
#flip_win = driver.window_handles[2]

#amazon---
global ama_price
global flp_Price
print(driver.title)
time.sleep(5)
ama_price = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
finalAMz= str(ama_price).replace("₹ ","").replace(",","").split(".")[0]
print("amazon price:"+ama_price)
if ama_price >= mobilePrice[0]:
    print("Amazon website price is greater")
else:
    print("Amazon website price is lesser")
driver.close()
driver.switch_to.window(parentWin)
time.sleep(4)
print(driver.title)
#Flipkart------
flipkartLnk = driver.find_element_by_xpath("//div[@class='prc-box prc-tbl--fullcards']/div[2]/div/div[3]/a")
flipkartLnk.click()
time.sleep(4)

childWindow1= driver.window_handles[1]
print(childWindow)
print(childWindow1)
driver.switch_to.window(childWindow1)


# driver.switch_to.window(amazon_win)
time.sleep(2)
flp_Price = driver.find_element_by_xpath("//div[contains(text(),'₹')]").text
finalFpkt = str(flp_Price).replace("₹","").replace(",","").split(".")[0]
print("flipkart price:"+flp_Price)
driver.close()
driver.switch_to.window(parentWin)



price = {}

price["Amazon"]=finalAMz
price["Flipkart"]=finalFpkt

for finalPrice in sorted(price.items()):
    print(finalPrice)




driver.quit()



    #def dclose()
    #driver.close()
#launchBrowser()

