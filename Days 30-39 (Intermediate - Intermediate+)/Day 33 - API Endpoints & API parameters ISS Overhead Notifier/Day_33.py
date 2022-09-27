# API REST

# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # ===================================================================================#
# # print(response.status_code)# 200 sucesso, 400 not found,
# # HTTP STATUS CODE https://www.webfx.com/web-development/glossary/http-status-codes/
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to acess this data.")
# # ====================================================================================#
# response.raise_for_status() # Já puxa o erro também
# # data = response.json()["iss_position"]["longitude"]# = posso fazer isso já que é um dicionario
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

from datetime import datetime

# API PARAMETERS
import requests

MINHA_LATITUDE = -23.550520
MINHA_LONGITUDE = -46.633308

parameters = {
    "lat": MINHA_LATITUDE,
    "lng": MINHA_LONGITUDE,
    # CHALLENGE PARTE
    "formatted": 0
}
# \/--------------ENDPOINT----------\/---PARAMETRO E VALOR--------\/
# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
r = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
r.raise_for_status()
data = r.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(":")
sunset = data["results"]["sunset"].split('T')[1].split(":")

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

# CHALLENGE = modifique a API desligando o formatador e colocando o tempo em estilo 24 horas
