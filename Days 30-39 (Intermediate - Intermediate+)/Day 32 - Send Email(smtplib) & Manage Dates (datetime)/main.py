##################### Hard Starting Project ######################
import datetime
import smtplib
from random import randint

import pandas

EMAIL = "renan@hotmail.com"
SENHA = ""

agora = datetime.datetime.now()
hoje_tuple = (agora.month, agora.day)
data = pandas.read_csv("birthdays.csv")

dia_data_aniversario = data["day"]
mes_data_aniversario = data["month"]

dic_aniversario = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if hoje_tuple in dic_aniversario:
    aniversariante = dic_aniversario[hoje_tuple]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", aniversariante["name"])

    with smtplib.SMTP("smtp.live.com") as conexao:
        conexao.starttls()
        conexao.login(EMAIL, SENHA)
        conexao.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: Parabains\n\n{contents}")
