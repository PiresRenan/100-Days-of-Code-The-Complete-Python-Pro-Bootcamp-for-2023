from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

chr_driver_path = "C:\Development\chromedriver.exe"
d = webdriver.Chrome(executable_path=chr_driver_path)

d.get(url="https://en.wikipedia.org/wiki/Main_Page")

n_articles = d.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

# n_articles.click()

contents = d.find_element(By.LINK_TEXT, "Contents")

# contents.click()

search = d.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)



























# d.quit()