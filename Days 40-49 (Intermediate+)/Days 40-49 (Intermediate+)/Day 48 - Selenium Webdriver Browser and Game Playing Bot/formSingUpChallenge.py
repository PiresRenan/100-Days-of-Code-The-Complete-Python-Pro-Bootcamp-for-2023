from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = "C:\Development\chromedriver.exe"
d = webdriver.Chrome(executable_path=driver_path)
d.get(url="http://secure-retreat-92358.herokuapp.com/")

objeto_ = d.find_element(By.NAME, "fName")
objeto_.send_keys("Renan")
objeto_ = d.find_element(By.NAME, "lName")
objeto_.send_keys("Pires")
objeto_ = d.find_element(By.NAME, "email")
objeto_.send_keys("renan.sp.121@hotmail.com")
objeto_ = d.find_element(By.XPATH, "/html/body/form/button")
objeto_.send_keys(Keys.ENTER)



