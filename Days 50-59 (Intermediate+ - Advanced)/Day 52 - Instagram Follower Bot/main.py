from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized')

class InstaFollower:

    def __init__(self, OPTIONS):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(3)
        # followers = self.driver.find_element(By.CSS_SELECTOR, '#mount_0_0_F6 > div > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div > div > div.alzwoclg.cqf1kptm.p1t2w4gn.fawcizw8.om3e55n1.g4tp4svg > section > main > div > header > section > ul > li:nth-child(2) > a')
        # followers.click()

        sleep(3)
        # modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(OPTIONS=options)
bot.login()
bot.find_followers()
# bot.follow()
