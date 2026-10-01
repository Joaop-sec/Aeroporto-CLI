from tkinter import *
from tkinter import ttk


def executar_janela_login(login_window):

    login_window.title("F22 - EXPRESS")

    login_window.geometry("600x500")
    #login_window.maxsize(width=900, height=600)
    #login_window.minsize(width=400, height=600)

    login_window.configure(bg="white")




    title = Label(
        text="⌯✈︎ | F22 - EXPRESS",
        font=("Ubuntu", 20, "bold"),
        fg="black",
        bg="white"
    
    )

    title.place(
        relx=0.5,
        rely=0.10,
        anchor=CENTER
    )

    title2 = Label(
        text="                   Sistema de gerenciamento aereo",
        font=("Arial", 8),
        fg="black",
        bg="white",
    )

    title2.place(
        relx=0.5,
        rely=0.14,
        anchor=CENTER
    )


    line = Label(
        text="───────────────────────────────────────────────────────────────",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    line.place(
        relx=0.5,
        rely=0.18,
        anchor=CENTER
    )

    logo = Label(
        login_window,
        text="👤 Área do Cliente",
        font=("Ubuntu", 15, "bold"),
        fg="black",
        bg="white"
    )
    logo.place(
        relx=0.5,
        rely=0.23,
        anchor=CENTER
    )



    sub1 = Label(
        login_window,
        text="Selecioe a opção no menu abaixo",
        font=("Arial", 10,),
        fg="black",
        bg="white"
    )
    sub1.place(
        relx=0.5,
        rely=0.30,
        anchor=CENTER
    )









'''

    subsub = Label(
        login_window,
        text="Digite seu e-mail para se inscrever no app",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )
    subsub.place(
        relx=0.5,
        rely=0.35,
        anchor=CENTER
    )

    subsub = Label(
        login_window,
        text="Digite seu e-mail para se inscrever no app",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )
    subsub.place(
        relx=0.5,
        rely=0.35,
        anchor=CENTER
    )


    campo_email = Entry(
        login_window,
        font=("Arial, 12"),
        fg="black",
        bg="white"
    )
    campo_email.insert(0, " email@dominio.com")

    campo_email.place(
        relx=0.5,
        rely=0.41,
        anchor=CENTER
    )


    botao_cadastra = Button(
        login_window,
        text="Cadastre-se com e-mail",
        font=("Arial, 12"),
        fg="black",
        bg="#D9D1D0"
    )

    botao_cadastra.place(
        relx=0.5,
        rely=0.50,
        anchor=CENTER
    )


    text_continue = Label(
        text="—— Ou continue com ——",
        font=("Arial, 9"),
        fg="black",
        bg="white"

    )

    text_continue.place(
        relx=0.5,
        rely=0.56,
        anchor=CENTER
    )

    botao_google = Button(
        login_window,
        text="GOOGLE",
        font=("Arial, 12"),
        fg="black",
        bg="#D9D1D0"
    )

    botao_google.place(
        relx=0.5,
        rely=0.63,
        anchor=CENTER
    )


    '''