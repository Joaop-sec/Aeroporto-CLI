from tkinter import *
from tkinter import ttk


def executar_janela_login(meus_dados):

    meus_dados.title("F22 - EXPRESS")

    meus_dados.geometry("600x500")
    #login_window.maxsize(width=900, height=600)
    #login_window.minsize(width=400, height=600)

    meus_dados.configure(bg="white")


#------------------------------------------------------------------

    title = Label(
        meus_dados,
        text="⌯✈︎ | F22 - EXPRESS",
        font=("Ubuntu", 15, "bold"),
        fg="black",
        bg="white"
    
    )

    title.place(
        relx=0.5,
        rely=0.10,
        anchor=CENTER
    )

#------------------------------------------------------------------
    line1 = Label(
        meus_dados,
        text="───────────────────────────────────────────────────────────────",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    line1.place(
        relx=0.50,
        rely=0.16,
        anchor=CENTER,
        relwidth=0.50
    )
#------------------------------------------------------------------
    text_meus_dados = Label(
        meus_dados,
        text="👤 Meus dados",
        font=("Ubuntu", 15, "bold"),
        fg="black",
        bg="white"
    )
    text_meus_dados.place(
        relx=0.5,
        rely=0.20,
        anchor=CENTER
    )
#------------------------------------------------------------------
    nome = Label(
        meus_dados,
        text="Nome:",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    nome.place(
        relx=0.1,
        rely=0.23,
        anchor=CENTER
    )

    campo_nome = Entry(
        font=("Arial, 12"),
        fg="black",
        bg="white"
    )
    campo_nome.insert(0, "Nome do usúario")

    campo_nome.place(
        relx=0.20,
        rely=0.30,
        anchor=CENTER,
        relwidth=0.20
    )
#------------------------------------------------------------------
    cpf = Label(
        meus_dados,
        text="CPF:",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    cpf.place(
        relx=0.1,
        rely=0.37,
        anchor=CENTER
    )

    campo_CPF = Entry(
        font=("Arial, 12"),
        fg="black",
        bg="white"
    )
    campo_CPF.insert(0, "CPF do usúario")

    campo_CPF.place(
        relx=0.20,
        rely=0.44,
        anchor=CENTER,
        relwidth=0.20
    )

#------------------------------------------------------------------

    ID = Label(
        meus_dados,
        text="ID",
        font=("Arial, 12"),
        fg="black",
        bg="white"
    )

    ID.place(
        relx=0.1,
        rely=0.50,
        anchor=CENTER
    )

    campo_ID = Entry(
        meus_dados,
        font=("Arial, 12"),
        fg="black",
        bg="white",
    )
    campo_ID.insert(0, "ID do cliente")

    campo_ID.place(
        relx=0.20,
        rely=0.57,
        anchor=CENTER,
        relwidth=0.20
    )

#------------------------------------------------------------------
    line2 = Label(
        meus_dados,
        text="───────────────────────────────────────────────────────────────",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    line2.place(
        relx=0.50,
        rely=0.70,
        anchor=CENTER,
        relwidth=0.50
    )

#------------------------------------------------------------------

    editar_dados = Button(
        meus_dados,
        text="Editar dados",
        font=("Arial, 10"),
        fg="black",
        bg="white"
    )

    editar_dados.place(
        relx=0.5,
        rely=0.80,
        anchor=CENTER
    )

#------------------------------------------------------------------

    voltar = Button(
        meus_dados,
        text="↩ Voltar",
        font=("Arial", 10),
        fg="black",
        bg="white"
    )

    voltar.place(
        relx=0.5,
        rely=0.90,
        anchor=CENTER
    )






if __name__ == "__main__":
    janela = Tk()
    executar_janela_login(janela)
    janela.mainloop()