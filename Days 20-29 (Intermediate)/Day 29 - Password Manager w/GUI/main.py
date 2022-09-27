import random
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SIMBOLOS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ';', ',', '=']


def generate_password():
    password_letters = [random.choice(LETRAS) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(SIMBOLOS) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(NUMEROS) for _ in range(random.randint(2, 4))]

    senha = password_letters + password_symbols + password_numbers
    random.shuffle(senha)

    senha_final = ''.join(senha)
    password_box.insert(0, senha_final)
    pyperclip.copy(senha_final)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if website_box.get() != '' and username_box.get() != '' and password_box.get() != '':
        website = website_box.get()
        email = username_box.get()
        password = password_box.get()
    else:
        messagebox.showerror(title="Erro", message="Preencha todos os campos para enviar de forma correta!")

    # messagebox.showinfo(title="Title", message="Message")
    is_ok = messagebox.askokcancel(title=website,
                                   message=f'Essas sao suas credenciais:\nEmail: {email}\nPassword:{password}.\nConfirma o salvar?')

    if is_ok:
        with open("data.txt", mode='a') as data:
            data.write(f"{website} | {email} | {password}\n")
        website_box.delete(0, END)
        password_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=189, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

website_box = Entry(width=52)
website_box.focus()
website_box.grid(column=1, row=1, columnspan=2)
username_box = Entry(width=52)
username_box.insert(0, "renan.sp.121@hotmail.com")
username_box.grid(columnspan=2, column=1, row=2)
password_box = Entry(width=34)
password_box.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(width=44, text="ADD", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
