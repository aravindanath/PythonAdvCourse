from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import platform
from webdriver_manager.chrome import ChromeDriverManager
import time
if platform.system() == "Windows":
     driver = Chrome(executable_path="D:\\Drivers\\chromedriver.exe")
elif platform.system() == "Darwin":
    driver = Chrome(ChromeDriverManager().install())
url = "https://demo.midtrans.com/"
driver.get(url)
driver.maximize_window()
buyNow = driver.find_element_by_link_text('BUY NOW')
buyNow.click()
time.sleep(5)
#-----------Shopping Cart--------
# innerWin = driver.find_element_by_xpath("//div[@id='container']/div/div/div[2]/div[1]")
innerWin = driver.find_element_by_css_selector(".cart-inner")
innerWin.click()
time.sleep(3)
# newWin = driver.find_element_by_xpath("//span[contains(text(),'Shopping Cart')]")
# newWin.send_keys(Keys.NULL)//div[4]/table/tbody/tr[1]/td[2]/input
Name = innerWin.find_element_by_xpath("div[4]/table/tbody/tr[1]/td[2]/input")
Name.clear()
#    "/div/div[4]/table/tbody/tr/td[contains(text(),'Name')]")
Name.send_keys("Jhon")
Email = innerWin.find_element_by_xpath("div[4]/table/tbody/tr[2]/td[2]/input")
Email.clear()
Email.send_keys("sample1@utomo.com")
Phone = innerWin.find_element_by_xpath("div[4]/table/tbody/tr[3]/td[2]/input")
Phone.clear()
Phone.send_keys("081808466411")
City = innerWin.find_element_by_xpath("div[4]/table/tbody/tr[4]/td[2]/input")
City.clear()
City.send_keys("Jakarta")
Address = innerWin.find_element_by_xpath("div[4]/table/tbody/tr[5]/td[2]/textarea")
Address.clear()
Address.send_keys("MidPlaza 2, 4th Floor Jl.Jend.Sudirman Kav.10-11")
PostalCode = innerWin.find_element_by_xpath("div[4]/table/tbody/tr[1]/td[2]/input")
PostalCode.send_keys("10220")
Checkout = driver.find_element_by_xpath("//div[@class='cart-checkout' and text()='CHECKOUT']")
Checkout.click()
currentWin = driver.current_window_handle
print(currentWin)
time.sleep(6)
#---------------Order Summary-----------
# currentWin1 = driver.current_window_handle
# print(currentWin1)
# acts = ActionChains(driver)
# headerTxt = driver.find_element_by_xpath("//*[@id='header']/div/h1").text
# print(headerTxt)
# OrderSummary = driver.find_element_by_xpath("//*[@id='application']/div[1]/a")
# acts.move_to_element(to_element=OrderSummary)
# OrderSummary.click()
driver.switch_to.frame("snap-midtrans")
time.sleep(2)
ContinueButton = driver.find_element_by_xpath("//span[text()='Continue']")
act =ActionChains(driver)
act.click(ContinueButton).perform()

CreditCard = driver.find_element_by_xpath("//div[text()='Credit Card']")
act.click(CreditCard).perform()
time.sleep(2)
CardNumber = driver.find_element_by_name("cardnumber")
CardNumber.send_keys("4811 1111 1111 1114")
ExpiryDate = driver.find_element_by_xpath("//input[@placeholder='MM / YY']")
ExpiryDate.send_keys("09/20")
CVV = driver.find_element_by_xpath("//input[@placeholder='123']")
CVV.send_keys("123")
PromoCode = driver.find_element_by_xpath("//input[@placeholder='123']")
PromoCode.click()
PayNow = driver.find_element_by_xpath("//span[text()='Pay Now']")
act.click(PayNow).perform()
time.sleep(5)