from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager



class TestCase01():

    def __init__(self):
        global driver
        driver = Chrome(ChromeDriverManager().install())


    def test_01(self):
        driver.get("https://www.google.com")

    def teardown(self):
        driver.quit()


t = TestCase01()
t.test_01()
t.teardown()