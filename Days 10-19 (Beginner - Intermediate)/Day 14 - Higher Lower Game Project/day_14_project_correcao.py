# Quebre o programa em pequenas partes.
import random

from arts import logo, vs
from game_data import data

# Mostrar a imagem.
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


# Formatar a lista para algo "User Friendly".
def format_data(account):
    """
    It takes a dictionary as an argument, and then prints out a formatted string based on the values of
    the dictionary
    :param account: The account object
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """
    If a has more followers than b, then the guess should be "a", otherwise the guess should be "b"
    :param guess: a string, either "a" or "b" representing which account has more followers
    :param a_followers: The number of followers of the first account
    :param b_followers: the number of followers of the account that you think has more followers
    :return: True or False
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Faça o jogo repetir.
# noinspection SpellCheckingInspection
while game_should_continue:
    # Gerar uma lista aleatória do game_data.

    # Faça a lista B se tornar a lista A para próxima pergunta.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Faça uma pergunta para o úsuario.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Cheque se o usuario esta correto.
    ##Pegue o numero de seguidores de cada conta.
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # Dar o feedback ao usuario.
    # Mantém a pontuação.
    if is_correct:
        # Mantém a pontuação.

        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
