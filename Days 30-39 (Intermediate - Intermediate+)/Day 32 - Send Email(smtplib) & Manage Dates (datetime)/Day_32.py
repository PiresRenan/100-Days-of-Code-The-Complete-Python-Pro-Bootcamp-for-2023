# Enviar emails de forma automatica e datetime module

#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="renan.sp.121@hotmail.com",
#         msg="Subject:Hello\n\nThis is the body of email.")
#
# # connection.close() # podemos substituir esse encerramento pelo mesmo metodo do open(...)


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2022:
    print("Ano de eleição e de Copa do Catar.")

print(month)
print(day_of_week)
print(now)
print(type(now))

date_of_birth = dt.datetime(year=1996, month=1, day=14, hour=22, minute=30)
print(date_of_birth)
