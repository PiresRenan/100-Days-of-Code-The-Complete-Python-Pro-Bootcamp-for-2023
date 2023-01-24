# # Importing the webdriver module from the selenium package.
from selenium import webdriver
# Importing the By class from the selenium.webdriver.common module.
from selenium.webdriver.common.by import By
# Importing the Service class from the selenium.webdriver.chrome.service module.
from selenium.webdriver.chrome.service import Service
# Importing the ChromeDriverManager class from the webdriver_manager.chrome module.
from webdriver_manager.chrome import ChromeDriverManager

# # Setting the path to the Chrome driver.
chrome_driver_path = "C:\Development\chromedriver.exe"

# # Creating a new instance of the Chrome driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Opening the Amazon website in the Chrome browser.
# driver.get("https://www.amazon.com")

# # It soft closes the browser.
# driver.close()

# # It hard closes the browser.
# driver.quit()

# ************************************


# Opening the Amazon website in the Chrome browser.
driver.get(url="https://www.amazon.com.br/Console-PlayStation-5-Digital-Edition/dp/B09FGCKBPK/ref=sr_1_5?keywords=playstation+5&qid=1662057437&sprefix=play%2Caps%2C264&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147")

# # Finding the element with the class name "a-price-symbol" and getting its text.
price_coin = driver.find_element(By.CLASS_NAME,"a-price-symbol").text
price_value = driver.find_element(By.CLASS_NAME,"a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME,"a-price-fraction").text
final_price = f"{price_coin} {price_value},{price_cents}"
print(final_price)



# driver.get("https://www.python.org")

# Finding the element with the name "q" and assigning it to the variable search_bar. Then it is
# printing the value of the attribute "placeholder" of the element.
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# Finding the element with the class name "python-logo" and printing its size.
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# Finding the element with the class name "documentation-widget" and then finding the element with the
# tag "a" inside it. Then it is printing the text of the element.
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# Finding the element with the id "site-map" and then finding the element with the tag "a" inside it.
# Then it is printing the text of the element.
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# *********************************************
# challenge

# Finding all the elements with the class name "event-widget" and then finding all the elements with
# the tag "time" inside it. Then it is finding all the elements with the class name "event-widget" and
# then finding all the elements with the tag "a" inside it. Then it is creating an empty dictionary
# called events. Then it is iterating through the list of elements with the tag "time" and creating a
# dictionary with the key "time" and the value of the text of the element. Then it is creating a
# dictionary with the key "name" and the value of the text of the element. Then it is printing the
# dictionary.
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time":event_times[n].text,
#         "name":event_names[n+1].text
#     }
# print(events)


# *********************************************






driver.quit()
