from tkinter import *
from tkinter import ttk


def executar_janela_login(login_window):

    login_window.title("F22 - EXPRESS")

    login_window.geometry("900x600")
    #login_window.maxsize(width=900, height=600)
    #login_window.minsize(width=400, height=600)

    login_window.configure(bg="white")


    logo = Label(
        login_window,
        text="F22 - EXPRESS",
        font=("Ubuntu", 26, "bold"),
        fg="black",
        bg="white"
    )
    logo.place(
        relx=0.5,
        rely=0.15,
        anchor=CENTER
    )


    sub = Label(
        login_window,
        text="Acessar App",
        font=("Arial", 14, "bold"),
        fg="black",
        bg="white"
    )
    sub.place(
        relx=0.5,
        rely=0.30,
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


