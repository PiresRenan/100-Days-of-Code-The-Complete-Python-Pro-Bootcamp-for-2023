# https://openweathermap.org/current
# Autentificação em API's
# USE PYTHONANYWHERE PARA AUTOMATIZAR A EXECUÇÃO DO CODIGO
import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
ACC_SID = ""
AUTH_TKN = ""

weather_params = {
    "lat": -23.550520,
    "lon": -46.633308,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACC_SID, AUTH_TKN)
    message = client.messages.create(
        body='Vai chover, pega casaco!',
        from_='whatsapp:+12407741577',
        to='whatsapp:+'
    )
    print(message.status)
