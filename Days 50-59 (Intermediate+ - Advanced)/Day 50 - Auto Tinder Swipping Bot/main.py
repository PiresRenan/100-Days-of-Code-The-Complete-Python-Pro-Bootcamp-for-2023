from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url="http://www.tinder.com")

sleep(3)
enter_btn = driver.find_element(By.CSS_SELECTOR, '#c-1560500889 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div.Mx\(28px\).Mx\(8px\)--m > a')
enter_btn.click()

sleep(3)
log_w_fb_btn = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
log_w_fb_btn.click()

sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')

email.send_keys("")
password.send_keys("")
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)


sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

sleep(5)

for n in range(100):
    sleep(3)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
            sleep(2)
        except NoSuchElementException:
            sleep(2)

# driver.quit()



sleep(300)
driver.quit()