from tkinter import *

window = Tk()
label = Label()
botao_1 = Button(text="Botão 1")
botao_2 = Button(text="Botão 2")
box = Entry()

window.title("Desafio da Grid")
window.minsize(width=500, height=300)
# Adicionando bordas
window.config(padx=100, pady=200)

label.config(text="Label aqui", font=("Arial", 16, "bold"))
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

botao_1.grid(column=1, row=1)
botao_2.grid(column=2, row=0)

box.config(width=10)
box.grid(column=3, row=2)

window.mainloop()
