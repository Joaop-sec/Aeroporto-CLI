from tkinter import *
from tkinter import ttk


def executar_janela_login(login_window):

    login_window.title("F22 - EXPRESS")

    login_window.geometry("600x500")
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







if __name__ == "__main__":
    janela = Tk()
    executar_janela_login(janela)
    janela.mainloop()