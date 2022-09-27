# Tratamento de erros e uso de arquivos JSON

# # FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# Palavras chaves para lidar com tratamento de excessões
# try: (Algo que deva rodar, mas há possibilidade de erro)
# except: (Faz isso caso seja uma excessão)
# else: (Faz isso se não houver excessões)
# finally: (Faz isso não importa oque aconteça)

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"Essa chave {error_message} não existe.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error that I made up.")

# Exemplo pratico
height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("A altura humana não deve ser maior que 3 metros.")
bmi = weight / height ** 2
print(bmi)
