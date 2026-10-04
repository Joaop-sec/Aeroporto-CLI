from tkinter import *
from tkinter import ttk


def executar_janela_login(consultar_voos):

    consultar_voos.title("F22 - EXPRESS")

    consultar_voos.geometry("600x500")

    consultar_voos.configure(bg="white")



    title = Label(
            consultar_voos,
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


    line1 = Label(
        consultar_voos,
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
        consultar_voos,
        text="🔍︎​ Consultar voos",
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

    sub_label = Label(
        consultar_voos,
        text="Pesquise e encontre o melhor voo para você",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )
    sub_label.place(
        relx=0.5,
        rely=0.25,
        anchor=CENTER
    )

#------------------------------------------------------------------

    origem = Label(
        consultar_voos,
        text="📍 Origem:",
        font=("Arial", 12),
        fg="Black",
        bg="white"
    )

    origem.place(
        relx=0.15,
        rely=0.35,
        anchor=CENTER
    )

#------------------------------------------------------------------

    campo_origem = Entry(
        consultar_voos,
        font=("Arial", 12),
        fg="Black",
        bg="white"
    )

    campo_origem.place(
        relx=0.25,
        rely=0.42,
        anchor=CENTER
    )

#------------------------------------------------------------------

    destino = Label(
        consultar_voos,
        text="📍 Destino:",
        font=("Arial", 12),
        fg="Black",
        bg="white"
    )

    destino.place(
        relx=0.60,
        rely=0.35,
        anchor=CENTER
    )

#------------------------------------------------------------------

    campo_destino = Entry(
        consultar_voos,
        font=("Arial", 12),
        fg="Black",
        bg="white"
    )

    campo_destino.place(
        relx=0.70,
        rely=0.42,
        anchor=CENTER
    )

#------------------------------------------------------------------

    data_de_ida = Label(
        consultar_voos,
        text="📅 Data de ida:",
        font=("Arial", 12),
        fg="Black",
        bg="white"
    )

    data_de_ida.place(
        relx=0.90,
        rely=0.35,
        anchor=CENTER
    )

#------------------------------------------------------------------

    data_de_ida = Entry(
        consultar_voos,
        font=("Arial", 12),
        fg="Black",
        bg="white"
    )

    data_de_ida.place(
        relx=0.90,
        rely=0.42,
        anchor=CENTER
    )