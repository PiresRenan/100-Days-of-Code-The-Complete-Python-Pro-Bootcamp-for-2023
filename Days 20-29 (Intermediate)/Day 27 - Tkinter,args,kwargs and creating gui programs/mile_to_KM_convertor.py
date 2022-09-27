from tkinter import *

FONT = ("Arial Narrow", 12, "bold")


def calcular():
    km = float(caixa.get()) * 1.60934
    label3.config(text=km)


w = Tk()
w.title("Conversor de milhas para KM")
w.minsize(300, 100)
w.config(padx=100, pady=20)

caixa = Entry()
caixa.insert(END, "0")
caixa.focus()
caixa.config(width=10, justify="center")
caixa.grid(column=1, row=0)

label1 = Label(text="milhas", font=FONT)
label1.grid(column=2, row=0)

label2 = Label(text="é igual a", font=FONT)
label2.grid(column=0, row=1)

label3 = Label(text="0", font=FONT)
label3.grid(column=1, row=1)

label4 = Label(text="KM.", font=FONT)
label4.grid(column=2, row=1)

botao = Button(text="Calcular", command=calcular)
botao.grid(column=1, row=2)

w.mainloop()

##  Correção  ##

# from tkinter import *
#
#
# def miles_to_km():
#     miles = float(miles_input.get())
#     km = round(miles * 1.609)
#     kilometer_result_label.config(text=f'{km}')
#
#
# window = Tk()
# window.title("Miles to Kilometer Converter")
# window.config(padx=20, pady=20)
#
# miles_input = Entry(width=7)
# miles_input.grid(column=1, row=0)
#
# miles_label = Label(text="Miles")
# miles_label.grid(column=2, row=0)
#
# is_equal_label = Label(text="is equal to")
# is_equal_label.grid(column=0, row=1)
#
# kilometer_result_label = Label(text="0")
# kilometer_result_label.grid(column=1, row=1)
#
# kilometer_label = Label(text="Km.")
# kilometer_label.grid(column=2, row=1)
#
# calculate_button = Button(text="Calculate", command=miles_to_km)
# calculate_button.grid(column=1, row=2)
#
# window.mainloop()
