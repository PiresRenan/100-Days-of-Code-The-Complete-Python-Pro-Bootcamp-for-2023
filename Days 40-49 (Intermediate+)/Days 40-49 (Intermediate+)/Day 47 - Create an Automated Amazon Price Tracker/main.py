from bs4 import BeautifulSoup
import requests
from twilio.rest import Client 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
amz_url = "https://www.amazon.com/PlayStation-5-Console/dp/B09DFCB66S/ref=sr_1_3?crid=XE5ACHN32L75&keywords=ps5&qid=1662040889&sprefix=ps5%2Caps%2C371&sr=8-3"
header = {"Accept-Language":"en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,es;q=0.6",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
          "Connection":"keep-alive"
          }
def send_message(price):
    message = client.messages.create( 
                            from_='whatsapp:+14155238886',  
                            body=f'Ta na hora de comprar, seu item está por apenas {price}!!!',      
                            to='whatsapp:+5511993597029' 
                        ) 
def get_amazon_price():
    resp = requests.get(url=amz_url, headers= header)
    soup = BeautifulSoup(resp.content, "lxml")
    price_unformatted = soup.find(name="span", class_="a-offscreen").getText()
    price = float(price_unformatted.split("$")[1])
    return price
if get_amazon_price() < 500.0 :
    send_message(get_amazon_price())
