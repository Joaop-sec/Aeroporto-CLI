
from tkinter import *
from pathlib import Path


def executar_gui_login(janela):

    janela.title("F22 - EXPRESS")

    janela.rowconfigure(0, weight=1)
    janela.columnconfigure(0, weight=1)

    # ─────────────────── Imagem de fundo ───────────────────

    pasta = Path(__file__).resolve().parent
    fundo = PhotoImage(file=str(pasta / "fundo.png"))

    label_fundo = Label(
        janela,
        image=fundo,
        bd=0
    )

    label_fundo.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    label_fundo.image = fundo

    # ─────────────────── Frame principal ───────────────────

    frame_principal = Frame(
        janela,
        bg="#F1EFEF",
        width=430,
        height=520
    )

    frame_principal.grid(
        row=0,
        column=0
    )

    frame_principal.grid_propagate(False)

    frame_principal.columnconfigure(0, weight=1)

    # A linha 7 absorve o espaço vertical disponível.
    # Isso mantém o cadastro na parte inferior.
    frame_principal.rowconfigure(7, weight=1)

    # ─────────────────── Título ───────────────────

    title = Label(
        frame_principal,
        text="⌯✈︎ | F22 - EXPRESS",
        font=("Ubuntu", 20, "bold"),
        fg="#172633",
        bg="#F1EFEF"
    )

    title.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=15,
        pady=(25, 8)
    )

    # ─────────────────── Subtítulo ───────────────────

    sub_titulo = Label(
        frame_principal,
        text="Acesse sua conta para continuar",
        font=("Arial", 12),
        fg="#697786",
        bg="#F1EFEF"
    )

    sub_titulo.grid(
        row=1,
        column=0,
        pady=(0, 25)
    )

    # ─────────────────── Função placeholder ───────────────────

    def adicionar_placeholder(campo, texto, senha=False):

        campo.insert(0, texto)
        campo.config(fg="#7B8490")

        def ao_entrar(event):

            if campo.get() == texto:
                campo.delete(0, END)
                campo.config(fg="#172633")

                if senha:
                    campo.config(show="*")

        def ao_sair(event):

            if campo.get() == "":
                campo.config(show="")
                campo.insert(0, texto)
                campo.config(fg="#7B8490")

        campo.bind("<FocusIn>", ao_entrar)
        campo.bind("<FocusOut>", ao_sair)

    # ─────────────────── Campo de e-mail ───────────────────

    campo_email = Entry(
        frame_principal,
        font=("Arial", 12),
        fg="#172633",
        bg="white",
        relief="solid",
        bd=1,
        highlightthickness=0
    )

    campo_email.grid(
        row=2,
        column=0,
        padx=25,
        pady=(0, 12),
        sticky="ew",
        ipady=9
    )

    adicionar_placeholder(
        campo_email,
        "  ✉  E-mail"
    )

    # ─────────────────── Campo de senha ───────────────────

    campo_senha = Entry(
        frame_principal,
        font=("Arial", 12),
        fg="#172633",
        bg="white",
        relief="solid",
        bd=1,
        highlightthickness=0
    )

    campo_senha.grid(
        row=3,
        column=0,
        padx=25,
        pady=(0, 15),
        sticky="ew",
        ipady=9
    )

    adicionar_placeholder(
        campo_senha,
        "  🔒  Senha",
        senha=True
    )

# ─────────────────── Botão entrar ───────────────────

    from GUI_conexões.botões_entrar__home import mudar_janela

    botao_entrar = Button(
        frame_principal,
        text="→  Entrar",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#172027",
        activebackground="#293944",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=lambda: mudar_janela(janela)
    )

    botao_entrar.grid(
        row=4,
        column=0,
        padx=25,
        pady=(0, 22),
        sticky="ew",
        ipady=8
    )

    




    

    # ─────────────────── Divisória ───────────────────

    frame_divisoria = Frame(
        frame_principal,
        bg="#F1EFEF"
    )

    frame_divisoria.grid(
        row=5,
        column=0,
        padx=25,
        pady=(0, 12),
        sticky="ew"
    )

    frame_divisoria.columnconfigure(0, weight=1)
    frame_divisoria.columnconfigure(2, weight=1)

    linha_esquerda = Frame(
        frame_divisoria,
        bg="#CDD2D8",
        height=1
    )

    linha_esquerda.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=(0, 10)
    )

    texto_divisoria = Label(
        frame_divisoria,
        text="Ou continue com",
        font=("Arial", 9),
        fg="#697786",
        bg="#F1EFEF"
    )

    texto_divisoria.grid(
        row=0,
        column=1
    )

    linha_direita = Frame(
        frame_divisoria,
        bg="#CDD2D8",
        height=1
    )

    linha_direita.grid(
        row=0,
        column=2,
        sticky="ew",
        padx=(10, 0)
    )

    # ─────────────────── Botão Google ───────────────────

    def entrar_google():
        print("Login com Google")

    botao_google = Button(
        frame_principal,
        text="🌐  Google",
        font=("Arial", 12, "bold"),
        fg="#172633",
        bg="white",
        activebackground="#E8EBEF",
        relief="solid",
        bd=1,
        cursor="hand2",
        command=entrar_google
    )

    botao_google.grid(
        row=6,
        column=0,
        padx=25,
        pady=(0, 10),
        sticky="ew",
        ipady=8
    )

    # ─────────────────── Área inferior ───────────────────

    # A linha 7 é expansível.
    # O cadastro fica na linha 8, junto à parte inferior.

    frame_cadastro = Frame(
        frame_principal,
        bg="#F1EFEF"
    )

    frame_cadastro.grid(
        row=8,
        column=0,
        pady=(0, 20)
    )

    # ─────────────────── Texto de cadastro ───────────────────

    texto_conta = Label(
        frame_cadastro,
        text="Não tem uma conta?",
        font=("Arial", 9),
        fg="#697786",
        bg="#F1EFEF"
    )

    texto_conta.grid(
        row=0,
        column=0
    )

# ─────────────────── Link: Login --> Criar conta  ───────────────────

    from GUI_conexões.criar_conta__entrar import abrir_cadastro

    criar_conta = Label(
        frame_cadastro,
        text="Cadastre-se",
        font=("Arial", 9, "underline"),
        fg="#172633",
        bg="#F1EFEF",
        cursor="hand2"
    )

    criar_conta.grid(
        row=0,
        column=1,
        padx=(5, 0)
    )

    criar_conta.bind(
        "<Button-1>",
        lambda event: abrir_cadastro(event, janela)
    )






