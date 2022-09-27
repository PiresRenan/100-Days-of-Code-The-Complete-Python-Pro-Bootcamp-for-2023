from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PROMISED_DOWN = 60.0
PROMISED_UP = 30.0
TWITTER_EMAIL = ""
TWITTER_CONF_USER = ""
TWITTER_PASSWORD = ""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized')

class InternetSpeedTwitterBot:
    def __init__(self, OPTIONS):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)
        self.up = 7.0
        self.down = 50.0
        self.internet_provider = ""
        
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
        sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        sleep(60)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.internet_provider = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]').text
    
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(2)
        user_confirmation = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_confirmation.send_keys(TWITTER_CONF_USER)
        user_confirmation.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        sleep(2)
        tweet_button1 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span')
        tweet_button1.click()
        
        sleep(2)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')

        tweet = f"Hey {self.internet_provider}, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        tweet_button.click()

        sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot(OPTIONS=options)
bot.get_internet_speed()
if float(bot.down) < float(PROMISED_DOWN) and float(bot.up) < float(PROMISED_UP):
    bot.tweet_at_provider()


