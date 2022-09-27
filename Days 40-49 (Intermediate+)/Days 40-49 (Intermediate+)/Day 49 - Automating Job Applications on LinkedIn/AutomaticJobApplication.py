import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ACC_EMAIL = ""
ACC_PASS = ""

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3250483657&geoId=92000000&keywords=developer%20Python&location=Mundialmente&refresh=true")

sign_btn = driver.find_element(By.LINK_TEXT, "Entrar")
sign_btn.click()

usrName_btn = driver.find_element(By.ID, "username")
usrName_btn.send_keys(ACC_EMAIL)

pass_btn = driver.find_element(By.ID, "password")
pass_btn.send_keys(ACC_PASS)
pass_btn.send_keys(Keys.ENTER)

apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_btn.click()

time.sleep(600)

# Daqui nao rola mais porque despadronizaram o envio de curriculo

driver.quit()

