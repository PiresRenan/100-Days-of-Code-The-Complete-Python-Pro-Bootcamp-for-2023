# Snake Game com comparação e registro de pontuação
# Como criar, ler, e editar arquivos de maneira autonoma.

## 1. Criar um .txt ou ter um arquivo e especificá-lo como abaixo
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# # Devemos sempre fechar para poupar recursos computacionais
# file.close()

# Podemos faze-lo assim para que já encerre após o uso
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Editar um arquivo,
# (mode="r" apenas read),
# (mode="w" para writable, substitui tudo o arquivo)
# (mode="a" para append, anexa o novo texto)
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNovo texto")

# f"Dear {nome},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nAngela"

# Criar novo arquivo
# with open("novo_arquivo.txt", mode="w") as file:
#     file.write("texto teste.")

# Caminho de pastas e arquivos Absolute File Path(Caminho absoluto) de uma pasta é quando mapeamos desde a raiz,
# ou seja, desde a unidade C: ou MacHD, EX: C:/Usuários/TI/PycharmProjects/PythonCertificate/Days 20-29/Day 24
# Working Directory(Diretório de trabalho), quando estamos dentro de uma pasta, o caminho é encurtado para a unidade
# onde está trabalho até a unidade onde deve ser efetuado o salvamento do novo arquivo Relative File Path(Caminho
# relativo), EX: (estou na pasta Days 20-29), para acessar um arquivo dentro da pasta Day 24, usasse ./Day 24/data.txt.
# Mas caso queira um arquivo que está na pasta anterior, ../PythonCertificate.txt


# Buscando um arquivo pelo caminho absoluto
# with open("C:/Users/TI/OneDrive - Candide Industria e Comercio Ltda/Ambiente de Trabalho/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Buscando um arquivo pelo caminho relativo
with open("../../../../OneDrive - Candide Industria e Comercio Ltda/Ambiente de Trabalho/my_file.txt") as file:
    contents = file.read()
    print(contents)
