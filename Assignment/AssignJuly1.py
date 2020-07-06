#how to print class attribute value,
from selenium import webdriver
import time
import pytest

#def launchBrowser():

driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
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
global flipkartLnk
print(driver.title)
time.sleep(5)
ama_price = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
print("amazon price:"+ama_price)
if ama_price >= mobilePrice[0]:
    print("Amazon website price is greater")
else:
    print("Amazon website price is lesser")
driver.close()
driver.switch_to.window(parentWin)
time.sleep(4)

#Flipkart------
flipkartLnk = driver.find_element_by_xpath("//div[@class='prc-box prc-tbl--fullcards']/div[2]/div/div[3]/a")
flipkartLnk.click()
time.sleep(4)
for eachwin in childWindow:
    driver.switch_to.window(eachwin)

# driver.switch_to.window(amazon_win)
flp_Price = driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div").text
print("flipkart price:"+flp_Price)
driver.close()
driver.switch_to.window(parentWin)



    #def dclose()
    #driver.close()
#launchBrowser()

