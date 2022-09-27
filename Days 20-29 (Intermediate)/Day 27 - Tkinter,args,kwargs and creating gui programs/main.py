from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I'm a Label", font=("Arial", 25, "bold"))
my_label.pack()

my_label["text"] = "New Text"  # Posso substituir a frase assim ou no modo abaixo, dá no mesmo.
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
# Desafio: Mude a função do botão para que ele mude o texto escrito na janela.
def clicked():
    texto = input.get()
    my_label.config(text=texto)
    # my_label.config(text="O Botão foi clicado")
    # print("Eu Cliquei")


button = Button(text="Click me", command=clicked)
button.grid(column=1, row=1)

# Captura de dados pela janela
input = Entry(width=10)
input.grid(column=2, row=2)
# Desafio: Quando o botão é pressionado, oque tiver digitado no input deve aparecer na janela.
# print(input.get())


window.mainloop()

# Usando o comando pack(), ele irá apenas colocar na janela de forma lógica, ou seja, do centro da primeira linha até o
# fim sendo, alterado pelos comandos "side=(left,right,bottom,top)"
# Já com o .place(x=n,y=n), podemos determinar qual será a posição dentro da janela
# Podemos também usar o .grid(column=n, row=n), onde separamos a janela em "pedaços" como de uma grid, sendo que ele
# automaticamente cria os espaços pela sequencia dada.
# NÃO SE PODE USAR O .pack() E O .grid() AO MESMO TEMPO
