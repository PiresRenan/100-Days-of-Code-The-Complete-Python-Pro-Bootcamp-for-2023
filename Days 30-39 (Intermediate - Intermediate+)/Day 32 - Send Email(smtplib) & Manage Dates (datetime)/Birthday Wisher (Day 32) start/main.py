import datetime as dt
import smtplib
from random import choice

EMAIL = "renan@gmail.com"
SENHA = ""

with open("quotes.txt", "r") as frases:
    FRASES = frases.readlines()
    frase_escolhida = choice(FRASES)


def definindo_dia():
    agora = dt.datetime.now()
    n_dia = agora.weekday()
    if n_dia == 0:
        return "Segunda-feira"
    elif n_dia == 1:
        return "Terça-feira"
    elif n_dia == 2:
        return "Quarta-feira"
    elif n_dia == 3:
        return "Quinta-feira"
    elif n_dia == 4:
        return "Sexta-feira"
    elif n_dia == 5:
        return "Sábado"
    else:
        return "Domingo"


dia = definindo_dia()
with smtplib.SMTP("smtp.gmail.com") as conexao:
    conexao.starttls()
    conexao.login(EMAIL, SENHA)
    conexao.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject: Motivação de {dia}\n\n{frase_escolhida}"
    )
