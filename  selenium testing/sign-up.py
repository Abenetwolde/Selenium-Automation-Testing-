import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


s=Service("C:\\Users\\User\\Downloads\\chromedriver.exe")
# webdriver.Chrome(service=s)
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
time.sleep(3)
driver.find_element(By.Name,"firstname").send_keys("testName")
driver.find_element(By.Name,"lastname").send_keys("testNamesecond")
driver.find_element(By.Name,"reg_email__").send_keys("testname@gmail.com")
driver.find_element(By.Name,"reg_email__").send_keys("testname@gmail.com")

driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("pass80110847")
driver.find_element(By.ID, "password_step_input").send_keys("pass80110847")
month= Select(driver.find_element(By.XPATH, "//select[@title='Month']"))
month.select_by_visible_text("jul")
day= Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text("06")
year= Select(driver.find_element(By.XPATH, "//select[@title='Year']"))
year.select_by_visible_text("1998")

driver.find_element(By.XPATH, "//label[text()='{}']".format("male")).click()

#Submit the details for signup
driver.find_element(By.NAME, "websubmit").click()

#closes the session
driver.quit()
