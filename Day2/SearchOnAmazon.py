from browser import setup as st

st.driver.get("https://www.google.com")
st.driver.find_element_by_name("q").send_keys("Selenium jobs")