# Criando classes
##Como bom costume, nomear as classes usando PascalCase ou seja, usando letra maiuscula para diferenciar cada palavra
class User:
    # ...
    # pass
    # Criar um construtor devesse nomea-lo com __init__ (uma função especial) e usar como declaração "self" para se
    # referir a propria classe.
    # def __init__(self):
    #     #Atributos da classe
    #     #podemos, por exemplo, criar um modo de avisar sempre que um novo objeto for criado para classe.
    #     print("Um novo usuario foi criado...")
    # Declarando outra variavel para o construtor podemos atribuir já para o o objeto.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # podemos criar um atrituto relacionado ao objeto
        self.seguidores = 0
        self.seguindo = 0
        print("Um novo usuario foi criado...")

    # #Assim podendo criar o objeto já com os atributos
    # user_1 = User("001","Renan")
    # print(user_1.username)
    # print(user_1.seguidores)
    # podemos criar metodos relacionados ao objeto direto da classe
    def seguir(self, user):
        user.seguidores += 1
        self.seguindo += 1


user_1 = User("001", "Renan")
user_2 = User("002", "Kamille")
user_1.seguir(user_2)
print(user_1.seguidores)
print(user_1.seguindo)
print(user_2.seguidores)
print(user_2.seguindo)

# #Posso criar um objeto da classe
# user_1 = User()
# #Criar um atributo para a classe
# user_1.id = "001"
# user_1.username = "Renan"
# print(user_1.username)


# #Criar outro objeto pra classe e usar os atributos da classe nele
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Angela"
# print(user_2.username)


# Criar funcoes e tudo mais fora da identação da classe
# def function():
#     #dirá que pode proceguir sem codigo
#     pass

# print("Hello")
