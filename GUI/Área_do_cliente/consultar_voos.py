from tkinter import *
from tkinter import ttk


def executar_janela_consultar_voos(consultar_voos):

    consultar_voos.title("F22 - EXPRESS")
    consultar_voos.geometry("600x500")
    consultar_voos.configure(bg="white")


    # ─────────────────── Configuração da janela ───────────────────

    consultar_voos.columnconfigure(0, weight=1)
    consultar_voos.rowconfigure(0, weight=0)
    consultar_voos.rowconfigure(1, weight=1)  # frame2 (menor, embaixo)
    consultar_voos.rowconfigure(2, weight=0)  # Botão voltar   
    # ─────────────────── Frame principal ───────────────────

    frame = Frame(
        consultar_voos,
        bg="white"
    )

    frame.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=30,
        pady=(20, 0)
    )


    # Configuração do Frame

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

# ─────────────────── Frame 2 ───────────────────

    frame2 = Frame(
        consultar_voos,
        bg="#D6D6D6",
    )


    frame2.grid(
        row=1,
        column=0,
        sticky="nsew",
        padx=40, #BORDAS LATERAIS
        pady=(1, 40) #BORDA DE BAIXO E CIMA
    )


    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.columnconfigure(2, weight=1)

    # ─────────────────── Título ───────────────────

    title = Label(
        frame,
        text="⌯✈︎ | F22 - EXPRESS",
        font=("Ubuntu", 15, "bold"),
        fg="black",
        bg="white"
    )

    title.grid(
        row=0,
        column=0,
        columnspan=3,
        pady=(0, 5),
        sticky="nsew"
    )


    # ─────────────────── Linha ───────────────────

    line1 = Label(
        frame,
        text="───────────────────────────────────────────────────────────────",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    line1.grid(
        row=1,
        column=0,
        columnspan=3,
        sticky="nsew"
    )


    # ─────────────────── Consultar voos ───────────────────

    text_meus_dados = Label(
        frame,
        text="🔍︎ Consultar voos",
        font=("Ubuntu", 15, "bold"),
        fg="black",
        bg="white"
    )

    text_meus_dados.grid(
        row=2,
        column=0,
        columnspan=3,
        pady=(10, 2),
        stick="nsew"
    )


    # ─────────────────── Subtítulo ───────────────────

    sub_label = Label(
        frame,
        text="Pesquise e encontre o melhor voo para você",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    sub_label.grid(
        row=3,
        column=0,
        columnspan=3,
        pady=(0, 20),
        stick="nsew"
    )


    # ─────────────────── Origem ───────────────────

    origem = Label(
        frame,
        text="📍 Origem:",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    origem.grid(
        row=4,
        column=0,
        pady=6
    )


    campo_origem = Entry(
        frame,
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    campo_origem.grid(
        row=5,
        column=0,
        padx=10,
        sticky="ew"
    )


    # ─────────────────── Destino ───────────────────

    destino = Label(
        frame,
        text="📍 Destino:",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    destino.grid(
        row=4,
        column=1,
        pady=3
    )


    campo_destino = Entry(
        frame,
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    campo_destino.grid(
        row=5,
        column=1,
        padx=10,
        sticky="ew"
    )


    # ─────────────────── Data ───────────────────

    data_de_ida = Label(
        frame,
        text="📅 Data de ida:",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    data_de_ida.grid(
        row=4,
        column=2,
        pady=3
    )


    campo_data_de_ida = Entry(
        frame,
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    campo_data_de_ida.grid(
        row=5,
        column=2,
        padx=10,
        sticky="ew"
    )



    # ─────────────────── Passageiros ───────────────────

    passageiros = Label(
        frame,
        text="👤 Passageiros:",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    passageiros.grid(
        row=7,
        column=0,
        pady=9
    )

    campo_passageiros = Entry(
        frame,
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    campo_passageiros.grid(
        row=8,
        column=0,
        padx=15,
        stick="ew"
    )

# ─────────────────── Classe ───────────────────

    classe = Label(
        frame,
        text="💼 Classe",
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    classe.grid(
        row=7, 
        column=1,
        pady=9
    )

    campo_classe = Entry(
        frame,
        font=("Arial", 12),
        fg="black",
        bg="white"
    )

    campo_classe.grid(
        row=8,
        column=1,
        padx=10,
        stick="ew"
    )

# ─────────────────── Buscar Voos ───────────────────

    buscar_voos = Button(
        frame, 
        text="⌕ Buscar Voos",
        font=("Arial", 13),
        fg="white",
        bg="black"
    )

    buscar_voos.grid(
        row=8,
        column=2,
        padx=9,
        stick="ew"
    )

# ─────────────────── Voos Disponiveis ───────────────────

    voos_disponiveis = Label(
        frame,
        text="✈︎ Voos Disponíveis",
        font=("Arial", 12, "bold"),
        fg="black",
        bg="white"
    )

    voos_disponiveis.grid(
        row=10,
        column=0,
        padx=1,
        sticky="nsew"
        
    )

# ─────────────────── Nenhum Voo Encontrado ───────────────────


    aviao = Label(
        frame2,
        text="✈",
        font=("Arial", 25),
        fg="black",
    )

    aviao.grid(
        row=1,
        column=1,
        pady=(2, 0)
    )
            

    mensagem_principal = Label(
        frame2,
        text="Nenhum voo encontrado.",
        font=("Arial"),
        fg="black"
    )

    mensagem_principal.grid(
        row=2,
        column=1,
        pady=(1, 0),
        sticky="nsew"
    )

    sub_mensagem = Label(
        frame2,
        text="Tente ajustar os filtros da sua busca.",
        font=("Arial, 8"),
        fg="black",
    )

    sub_mensagem.grid(
        row=3,
        column=1,
        pady=(0, 10),
        stick="ew"
    )


# ─────────────────── Nenhum Voo Encontrado ───────────────────


    botão_voltar = Button(
        consultar_voos,
        text=("← Voltar"),
        font=("Arial", 13),
        fg="white"
    )

    botão_voltar.grid(
        row=2,
        column=0,
        sticky="ns",
        padx=40,
        pady=(0, 15)
    )






if __name__ == "__main__":
    janela = Tk()
    executar_janela_consultar_voos(janela)
    janela.mainloop()