from selenium.webdriver import Chrome,Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.wikipedia.org/")
lang =driver.find_elements_by_css_selector("#searchLanguage>option")
print("Total no of Lang:", len(lang))
empty=[]
for l in lang:
    empty.append(l.text)

print("UnSorted list",empty)
empty.sort()
print("Sorted list",empty)

driver.quit()



