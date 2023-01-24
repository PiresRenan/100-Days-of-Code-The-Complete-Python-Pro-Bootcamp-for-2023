import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
d.get(url="https://orteil.dashnet.org/experiments/cookie/")


def clickCookie():
    clicks = d.find_element(By.XPATH, '//*[@id="cookie"]')
    clicks.click() 
  
def upgrade():
    if int(d.find_element(By.CSS_SELECTOR, "#buyTime\ machine").text.split(" ")[3].split()[0].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyTimeMachine()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyPortal > b").text.split(" ")[2].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyPortal()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab > b").text.split(" ")[3].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyAlchemyLab()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyShipment > b").text.split(" ")[2].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyShipment()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyMine > b").text.split(" ")[2].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyMine()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyFactory > b").text.split(" ")[2].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyFactory()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyGrandma > b").text.split(" ")[2].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyGrandma()
    elif int(d.find_element(By.CSS_SELECTOR, "#buyCursor > b").text.split(" ")[2].replace(",", "")) <= int(d.find_element(By.ID, "money").text.replace(",", "")):
        buyNewCursor()
    else:
        pass
            
def clickCursorUpgrade():
    clicks = d.find_element(By.XPATH, '//*[@id="buyCursor"]')
    clicks = d.find_element(By.XPATH, '//*[@id="buyCursor"]/b/text()[2]')
    clicks.click()
    
def buyNewCursor():
    clicks = d.find_element(By.XPATH, '//*[@id="buyCursor"]')
    clicks.click()
    
def buyGrandma():
    clicks = d.find_element(By.XPATH, '//*[@id="buyGrandma"]')
    clicks.click()

def buyFactory():
    clicks = d.find_element(By.XPATH, '//*[@id="buyFactory"]')
    clicks.click()
    
def buyMine():
    clicks = d.find_element(By.XPATH, '//*[@id="buyMine"]')
    clicks.click()     

def buyShipment():
    clicks = d.find_element(By.XPATH, '//*[@id="buyShipment"]')
    clicks.click()

def buyAlchemyLab():
    clicks = d.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
    clicks.click()
    
def buyPortal():
    clicks = d.find_element(By.XPATH, '//*[@id="buyPortal"]')
    clicks.click()

def buyTimeMachine():
    clicks = d.find_element(By.XPATH, '//*[@id="buyTime machine"]')
    clicks.click()

timeout = time.time() + 60*5
up_time = time.time() + 5
while True:
    if time.time() > timeout:
        break
    elif time.time() > up_time:
        upgrade()
    else:
        clickCookie()

# print(int(d.find_element(By.ID, "money").text.replace(",", "")))


