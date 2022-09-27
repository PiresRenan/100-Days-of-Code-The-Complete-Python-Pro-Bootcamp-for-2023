from cafeteira import CoffeeMaker
from caixa import MoneyMachine
from menu import Menu

caixa = MoneyMachine()
cafeteira = CoffeeMaker()
menu = Menu()

ligado = True

while ligado:
    opcoes = menu.get_items()
    escolha = input(f"O que gostaria de beber?\n({opcoes}): ")
    if escolha == "off":
        ligado = False
    elif escolha == "report":
        cafeteira.report()
        caixa.report()
    else:
        bebida = menu.find_drink(escolha)
        if cafeteira.is_resource_sufficient(bebida) and caixa.make_payment(bebida.cost):
            cafeteira.make_coffee(bebida)
