from tkinter import *
from tkinter import ttk

def executar_janela_home(janela_home): 
    
    
    
    janela_home.title("F22 - EXPRESS")
    janela_home.geometry("600x500")
    janela_home.configure(bg="white")

# ─────────────────── Configuração da janela ───────────────────

    janela_home.columnconfigure(0, weight=1)
    janela_home.rowconfigure(0, weight=0)


#  ─────────────────── Cabeçalho  ───────────────────

    frame_topo = Frame(
        janela_home,
        bg="white"
    )

    frame_topo.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=30,
        pady=(20, 10)
    )

    frame_topo.columnconfigure(0, weight=1)

 # ─────────────────── Título ───────────────────

    title = Label(
    frame_topo,
    text="⌯✈︎ | F22 - EXPRESS",
    font=("Ubuntu", 15, "bold"),
    fg="black",
    bg="white"
    )

    title.grid(
        row=0,
        column=0,
        sticky="w"
    )

    # ─────────────────── Linha ───────────────────

    linha = Frame(
        frame_topo,
        bg="black",
        height=1
    )
    linha.grid(
        row=1,
        column=0,
        sticky="ew",
        pady=(12, 0)
    )

    # ─────────────────── Frame principal ───────────────────

    frame_principal = Frame(
        janela_home,
        bg="white"
    )

    frame_principal.grid(
        row=1,
        column=0,
        sticky="nsew",
        padx=30,
        pady=10
    )

    frame_principal.columnconfigure(0, weight=1) 

  # ─────────────────── Titulo 2 ───────────────────

    boas_vindas = Label(
        frame_principal,
        text="Bem vindo ao F22 - EXPRESS",
        font=("Ubuntu", 20, "bold"),
        fg="black",
        bg="white"
    )

    boas_vindas.grid(
        row=0,
        column=0,
        sticky="w",
        pady=(5, 5)
    )

    # ───────────────────  Sub Titulo 2 ───────────────────

    sub_title = Label(
        frame_principal,
        text="Sua próxima viagem começa aqui.",
        font=("Arial", 12),
        fg="gray",
        bg="white"
    )

    sub_title.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(0, 20)
    )

# ─────────────────── Frame 2 ───────────────────

    frame_destaque = Frame(
        frame_principal,
        bg="#D6D6D6",
        padx=20,
        pady=20
    )


    frame_destaque.grid(
        row=2,
        column=0,
        sticky="ew",
        pady=(0, 20) #BORDA DE BAIXO E CIMA
    )

    frame_destaque.columnconfigure(0, weight=1)

#  ─────────────────── Avião ───────────────────

    avião = Label(
        frame_destaque,
        text="✈︎",
        font=("Arial, 35"),
        fg="black"
    )

    avião.grid(
        row=0,
        column=0,
        sticky="w"
    )

# ─────────────────── Título Frame2 ───────────────────

    texto_destaque = Label(
         frame_destaque,
         text="Planeje sua próxima viagem",
         font=("Ubuntu", 15, "bold"),
         fg="black"
     )
 
    texto_destaque.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(5, 5)
    )

# ─────────────────── Sub Título Frame2 ───────────────────

    sub_titulo_f2 = Label(
        frame_destaque,
        text="Encontre voos e escolha seu próximo destino.",
        font=("Arial", 11),
        fg="#333333",
        bg="#D6D6D6"
     )
 
    sub_titulo_f2.grid(
        row=2,
        column=0,
        sticky="w",
        pady=(0, 12)
    )

# ─────────────────── Botão "Sobre Nós" ───────────────────

    botão_sobre_nós = Button(
        frame_destaque,
        text="ⓘ Sóbre nós",
        font=("Ubuntu", 11, "bold"),
        fg="white",
        bg="black"
        
     )
 
    botão_sobre_nós.grid(
        row=3,
        column=0,
        sticky="w"
    )
    
# ─────────────────── Opções - Navegação ───────────────────

    frame_opcoes = Frame(
        frame_principal,
        bg="white"
    )

    frame_opcoes.grid(
        row=3,
        column=0,
        sticky="nsew"
    )

    for coluna in range(3):
        frame_opcoes.columnconfigure(coluna, weight=1)

# ─────────────────── Opc1 - Consultar Voos ───────────────────

    opc_consultar = Button(
        frame_opcoes,
        text="✈︎\nConsultar Voos",
        font=("Arial", 11, "bold"),
        fg="black",
        bg="white"
    )

    opc_consultar.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=(0, 5),
        ipady=15
    )


# ─────────────────── Opc2 - Minhas reservas ───────────────────


    opc_reservas = Button(
        frame_opcoes,
        text="💼\nMinhas Reservas",
        font=("Arial", 11, "bold"),
        fg="black",
        bg="white"
    )

    opc_reservas.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=(0, 5),
        ipady=15
    )

# ─────────────────── Opc3 - Meus Dados ───────────────────

    opc_dados = Button(
        frame_opcoes,
        text="👤\nMeus Dados",
        font=("Arial", 11, "bold"),
        fg="black",
        bg="white"
    )

    opc_dados.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=(0, 5),
        ipady=15
    )

# ─────────────────── Rodapé ───────────────────

    rodape = Label(
        janela_home,
        text="F22 - EXPRESS | Seu sonho começa aqui!",
        font=("Arial", 9),
        fg="gray",
        bg="white"
    )

    rodape.grid(
        row=2,
        column=0,
        sticky="ew",
        pady=(5, 15)
    )






if __name__ == "__main__":
    janela = Tk()
    executar_janela_home(janela)
    janela.mainloop()    