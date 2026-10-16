from tkinter import *
from tkinter import ttk


def executar_janela_login(meus_dados):

    meus_dados.title("F22 - EXPRESS")
    #meus_dados.geometry("600x500")
    meus_dados.configure(bg="white")

# ─────────────────── Configuração da janela ───────────────────

    meus_dados.columnconfigure(0, weight=1)
    meus_dados.rowconfigure(0, weight=0)

#  ─────────────────── Cabeçalho  ───────────────────

    frame_topo = Frame(
        meus_dados,
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
        meus_dados,
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
        text="👤 Meus dados",
        font=("Ubuntu", 20, "bold"),
        fg="black",
        bg="white"
    )

    boas_vindas.grid(
        row=0,
        column=0,
        sticky="w",
        pady=(0, 5)
    )

    # ───────────────────  Sub Titulo 2 ───────────────────

    sub_title = Label(
        frame_principal,
        text="Aqui estão as informações da sua conta.",
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

# ─────────────────── Painel de destaque ───────────────────

    painel_destaque = Frame(
        frame_principal,
        bg="#D6D6D6",
        padx=20,
        pady=20
    )


    painel_destaque.grid(
        row=2,
        column=0,
        sticky="nsew",

    )

    painel_destaque.columnconfigure(0, weight=1)
    painel_destaque.columnconfigure(1, weight=1)

# ─────────────────── Frame Perfil ───────────────────

    painel_perfil = Frame(
        painel_destaque,
        bg="#D6D6D6"
        )

    
    painel_perfil.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(0, 20)
    )

#  ─────────────────── Foto ───────────────────

    foto = Label(
        painel_perfil,
        text="👤",
        font=("Arial", 40),
        fg="black",
        bg="gray",
        width=3,
        height=2
    )

    foto.grid(
        row=0,
        column=0,
        rowspan=3,
        padx=(0, 20)
    )

#  ─────────────────── Nome do user ───────────────────

    nome_user = Label(
        painel_perfil,
        text="João Pedro",
        font=("Arial", 22, "bold"),
        fg="black",
        bg="#D6D6D6"
    )

    nome_user.grid(
        row=0,
        column=1,
        sticky="w" 
    )

#  ─────────────────── E-mail do user ───────────────────

    email_user = Label(
        painel_perfil,
        text="joao@email.com",
        font=("Arial", 11),
        fg="black",
        bg="#D6D6D6"
    )

    email_user.grid(
        row=1,
        column=1,
        sticky="w",
        pady=3

    )

#  ─────────────────── Tipo de user ───────────────────

    tipo_usuario = Label(
        painel_perfil,
        text="Cliente",
        font=("Arial", 10),
        fg="#333333",
        bg="gray",
        padx=10,
        pady=3
    )
    tipo_usuario.grid(
        row=2,
        column=1,
        sticky="w",
        pady=(3, 0)
    )

#  ─────────────────── Divisa ───────────────────

    divisa = Frame(
        painel_destaque,
        bg="#B7B1B1",
        height=1
    )

    divisa.grid(
        row=1,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(0, 20)
    )

#  ─────────────────── Frame Coluna Esquerda ───────────────────

    coluna_esquerda = Frame(
        painel_destaque,
        bg="#D6D6D6"
    )

    coluna_esquerda.grid(
        row=2,
        column=0,
        sticky="nsew",
        padx=(0, 20)
    )

    coluna_esquerda.columnconfigure(1, weight=1)


    def criar_informacao(pai, linha, icone, titulo, valor):

        Label(
            pai,
            text=icone,
            font=("Arial", 20),
            fg="black",
            bg="#D6D6D6",
            width=3
        ).grid(
            row=linha,
            column=0,
            sticky="nw",
            padx=(0, 12),
            pady=(0, 18)
        )

#  ─────────────────── Bloco ───────────────────

        bloco = Frame(
            pai,
            bg="#D6D6D6"
        )

        bloco.grid(
            row=linha,
            column=1,
            sticky="ew",
            pady=(0, 18)
        )

#  ─────────────────── Titulo ───────────────────

        Label(bloco,
              text=titulo,
              font=("Arial, 11"),
              fg="black",
              bg="#D6D6D6",
            ).pack(anchor="w")

#  ─────────────────── Valor ───────────────────
        Label(
            bloco,
            text=valor,
            font=("Arial", 12),
            fg="black",
            bg="#D6D6D6",
            wraplength=250,
            justify="left"
        ).pack(anchor="w", pady=(3, 0))

#  ─────────────────── Campo Email - Uso da função ───────────────────

    criar_informacao(
        coluna_esquerda,
        0,
        "✉",
        "Email",
        "Email@exemplo.com"
    )

#  ─────────────────── Campo nome - Uso da função ───────────────────

    criar_informacao(
        coluna_esquerda,
        1, 
        "👤",
        "nome",
        "João Pedro"
    )

#  ─────────────────── Campo CPF - Uso da função ───────────────────

    criar_informacao(
        coluna_esquerda,
        2, 
        "▤",
        "CPF",
        "123.456.789-10"
    )


#  ─────────────────── Frame Coluna Direita ───────────────────

    coluna_esquerda = Frame(
        painel_destaque,
        bg="#D6D6D6"
    )

    coluna_esquerda.grid(
        row=2,
        column=1,
        sticky="nsew",
        padx=(0, 20)
    )

    coluna_esquerda.columnconfigure(1, weight=1)

#  ─────────────────── Campo Email - Uso da função ───────────────────

    criar_informacao(
        coluna_esquerda,
        0,
        "▤",
        "ID do cliente",
        "F22-000123"
    )

#  ─────────────────── Campo nome - Uso da função ───────────────────

    criar_informacao(
        coluna_esquerda,
        1, 
        "☎",
        "Telefone",
        "89-31244-1221"
    )

#  ─────────────────── Campo CPF - Uso da função ───────────────────

    criar_informacao(
        coluna_esquerda,
        2, 
        "⌖",
        "Endereço",
        "Rua: Ex, 123 - Centro - Macéio, AL"
    )

#  ─────────────────── Rodapé ───────────────────

    rodape = Frame(meus_dados, bg="white")
    rodape.grid(
        row=2,
        column=0,
        sticky="ew",
        padx=40,
        pady=(20, 25)
    )

    rodape.columnconfigure(0, weight=1)

#  ─────────────────── Linha - Rodapé ───────────────────

    linha_rodape = Frame(
        rodape,
        bg="#CCCCCC",
        height=1
    )

    linha_rodape.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(0, 20)

    )

#  ─────────────────── Botão voltar ───────────────────

    botao_voltar = Button(
        rodape,
        text="←  Voltar",
        font=("Arial", 12, "bold"),
        fg="black",
        bg="white"
    )

    botao_voltar.grid(
        row=1,
        column=0,
        sticky="w",
        ipadx=20,
        ipady=8
    )

#  ─────────────────── Botão Editar ───────────────────
    botao_editar = Button(
        rodape,
        text="✎  Editar dados",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="black"
    )

    botao_editar.grid(
        row=1,
        column=0,
        sticky="e",
        ipadx=20,
        ipady=8
    )


if __name__ == "__main__":
    janela = Tk()
    executar_janela_login(janela)
    janela.mainloop()