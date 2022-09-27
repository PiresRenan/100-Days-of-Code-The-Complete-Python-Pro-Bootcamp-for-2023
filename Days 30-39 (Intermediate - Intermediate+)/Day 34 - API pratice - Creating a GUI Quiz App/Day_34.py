# import requests
# # usando uma api diferente podemos ver a mesma estrutura de antes
# # -------------------\/----------ENDPOINT--------\/--PARAMETERS------------------------------------\/
# r = requests.get(url="https://opentdb.com/api.php?amount=50&category=17&difficulty=hard&type=boolean")
# r.raise_for_status()

# Em Python podemos apenas declarar um tipo de dado a ser esperado
# age: int
# name: str
# height: float
# is_human: bool

# Essa função, diz que sempre terá um retorno booleano, chamada função lambda
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine.")
