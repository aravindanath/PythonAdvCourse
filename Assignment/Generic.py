from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select


def acceptAlert(driver):
    alt = Alert(driver)
    print(alt.text)
    alt.accept()

def dismissAlert(driver):
    alt = Alert(driver)
    print(alt.text)
    alt.dismiss()

def sendValueToAlert(driver,value):
    alt = Alert(driver)
    print(alt.text)
    alt.send_keys(value)
    alt.accept()

def selectByIndexIndropdown(element,i):
    sel = Select(element)
    sel.select_by_index(i)

def selectByVisibleTextIndropdown(element,value):
    sel = Select(element)
    sel.select_by_visible_text(value)

def selectByValueIndropdown(element,value):
    sel = Select(element)
    sel.select_by_value(value)

def deSelectAll(ele):
    sel = Select(ele)
    sel.deselect_all()


def deSelectByIndexinDropdown(ele,i):
    sel = Select(ele)
    sel.deselect_by_index(i)


def deSelectByValueinDropdown(ele,value):
    sel = Select(ele)
    sel.deselect_by_value(value)

def deSelectByVisibleTextinDropdown(ele,value):
    sel = Select(ele)
    sel.deselect_by_visible_text(value)

def takeScreenShot(driver,file):
    driver.save_screenshot(file+".png")

def mouseHover(driver,ele):
    act = ActionChains(driver)
    act.move_to_element(ele).perform()

def actionClick(driver,ele):
    act = ActionChains(driver)
    act.click(ele).perform()

def dragNDrop(driver,src,dst):
    act = ActionChains(driver)
    act.drag_and_drop(src,dst).perform()

def rightClikc(driver,ele):
    act = ActionChains(driver)
    act.context_click(ele).perform()