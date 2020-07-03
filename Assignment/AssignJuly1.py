from selenium import webdriver
import pytest

def launchBrowser():

    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
    Url = "https://www.mysmartprice.com/mobile/apple-iphone-xir-msp15688"
    driver.get(Url)
    driver.maximize_window()
def findPrice():
    productName = driver.find_element_by_xpath("//h1[@class='prdct-dtl__ttl']").text
    print(productName)
    AmzPrice= driver.find_element_by_xpath("//div[@data-storename='amazon']/div/div[2]").text
    print("Amazon Price:"+AmzPrice)
    fkartPrice = driver.find_element_by_xpath("//div[@data-storename='flipkart']/div/div[2]").text
def comparePrice():
    print("Flipkart Price is:" + fkartPrice.replace("1", ""))

def close
    driver.close()
