from tkinter import *

# Criando a janela
janela = Tk()
janela.title("Exemplos de Widgets do Tkinter")
janela.minsize(500, 500)

# Labels
my_label = Label(text="Texto inicial", font=("Arial", 20, "italic"))
my_label.config(text="Esse o Texto para substituir o inicial.")
my_label.pack()


# Botões
def action():
    print("Faz alguma coisa!")


# Chamada de função pelo botão
botao = Button(text="Clique aqui", command=action)
botao.pack()

# Caixas de dialogo
caixa_de_entrada = Entry(width=30)
# texto inicial na box
caixa_de_entrada.insert(END, string="Algum texto inicia aqui.")
# pegando o texto digitado na box
print(caixa_de_entrada.get())
caixa_de_entrada.pack()

# Caixa de texto
caixa_de_texto = Text(height=5, width=35)
# Jogando o cursor para a caixa de texto
caixa_de_texto.focus()
# adicionando um texto inicial
caixa_de_texto.insert(END, "Exemplo de uma entrada de um texto com multiplas linhas.")
# capturando os dados da caixa de texto, onde a string "1.0" representa que o texto a ser pego é o da primeira
# linha e do caracter de index 0
print(caixa_de_texto.get("1.0", END))
caixa_de_texto.pack()


# Caixa rotativa
def spinbox_used():
    # pega o valor equivalente na caixa rotativa.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Escalar
# Chamada com o respectivo valor escalar
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Botão de check
def checkbutton_used():
    # printa 1 se o botao estiver checado, ou 0 se nao
    print(checked_state.get())


# Uma variavel para manter o estado da caixa de check
checked_state = IntVar()
checkbutton = Checkbutton(text="Está ligado?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Botao de Radio
def radio_used():
    print(radio_state.get())


# Variavel para assegurar qual dos botoes esta sendo checado
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Opção 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Opção 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Caixa de lista
def listbox_used(event):
    # Captura o que foi selecionado dentro da box
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Maçã", "Pêra", "Laranja", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

janela.mainloop()
