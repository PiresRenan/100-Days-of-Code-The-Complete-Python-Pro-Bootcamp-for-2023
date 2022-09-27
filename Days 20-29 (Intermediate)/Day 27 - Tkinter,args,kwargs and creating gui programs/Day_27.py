# Graphical User Interface(GUI) com Tkinter e Argumentos funcionais (*Args e ** Kwargs)
# import do modulo
# import tkinter

# criando um objeto a partir da classe dentro do módulo
# window = tkinter.Tk()
# window.title("Meu primeiro programa com GUI")  # nome da janela
# window.minsize(width=500, height=300)  # tamanho

# Label
# my_label = tkinter.Label(text="Eu sou uma label", font=("Arial Black", 24, "italic"))  # Criando
# my_label.pack(side="left")  # adicionando na janela (side="bottom" == posição), (expand=True == a janela toda e
# centraliza), para mais "http://tcl.tk/man/tcl8.6/TkCmd/pack.htm"


# Mantém a janela aberta
# window.mainloop()


# Em Python existe a argumentação padrão de um metodo, o que garante que não precise colocar todos os argumentos na
# chamada do metodo, caso queira trocar é apenas colocar a palavra chave do argumento seguido do que deseja.
# def add(n1=4, n2=9):
#    return n1 + n2


# print(add())  # Usando a argumentação padrão do método.
# print(add(n2=15))  # Substituindo o valor de um e usando o outro padrão.
# print(add(n1=5, n2=3))  # Substituindo ambos valores, sem deixar o padrão.

# Para usar valores ilimitados de argumentos *args, ex.
def show(*args):
    for n in args:
        print(n)


show(5, 6, 9, 4)
