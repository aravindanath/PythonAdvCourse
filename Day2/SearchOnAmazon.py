from browser import setup as st

st.driver.get("https://www.amazon.com")
# st.driver.find_element_by_name("q").send_keys("Selenium jobs")

st.driver.execute_script("arguments[0].scrollHeight;")
st.driver.current_url