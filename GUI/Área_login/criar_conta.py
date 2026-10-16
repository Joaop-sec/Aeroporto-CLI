
from tkinter import *
from pathlib import Path


def executar_gui_cadastro(janela):

    # ─────────────────── Limpar janela anterior ───────────────────

    for widget in janela.winfo_children():
        widget.destroy()

    janela.title("F22 - EXPRESS | Criar conta")

    janela.rowconfigure(0, weight=1)
    janela.columnconfigure(0, weight=1)

    # ─────────────────── Carregar imagem de fundo ───────────────────

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
        height=580
    )

    frame_principal.grid(
        row=0,
        column=0
    )

    frame_principal.grid_propagate(False)
    frame_principal.columnconfigure(0, weight=1)

    # Espaço flexível para manter o link embaixo
    frame_principal.rowconfigure(7, weight=1)

    # ─────────────────── Título ───────────────────

    titulo = Label(
        frame_principal,
        text="⌯✈︎ | F22 - EXPRESS",
        font=("Ubuntu", 20, "bold"),
        fg="#172633",
        bg="#F1EFEF"
    )

    titulo.grid(
        row=0,
        column=0,
        pady=(22, 5)
    )

    # ─────────────────── Subtítulo ───────────────────

    subtitulo = Label(
        frame_principal,
        text="Crie sua conta para começar",
        font=("Arial", 12),
        fg="#697786",
        bg="#F1EFEF"
    )

    subtitulo.grid(
        row=1,
        column=0,
        pady=(0, 22)
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

# ─────────────────── Campo nome ───────────────────

    campo_nome = Entry(
        frame_principal,
        font=("Arial", 12),
        fg="#172633",
        bg="white",
        relief="solid",
        bd=1
    )

    campo_nome.grid(
        row=2,
        column=0,
        padx=25,
        pady=(0, 12),
        sticky="ew",
        ipady=9
    )

    adicionar_placeholder(
        campo_nome,
        "  Nome completo"
    )

# ─────────────────── Campo e-mail ───────────────────

    campo_email = Entry(
        frame_principal,
        font=("Arial", 12),
        fg="#172633",
        bg="white",
        relief="solid",
        bd=1
    )

    campo_email.grid(
        row=3,
        column=0,
        padx=25,
        pady=(0, 12),
        sticky="ew",
        ipady=9
    )

    adicionar_placeholder(
        campo_email,
        "  E-mail"
    )

# ─────────────────── Campo senha ───────────────────

    campo_senha = Entry(
        frame_principal,
        font=("Arial", 12),
        fg="#172633",
        bg="white",
        relief="solid",
        bd=1
    )

    campo_senha.grid(
        row=4,
        column=0,
        padx=25,
        pady=(0, 12),
        sticky="ew",
        ipady=9
    )

    adicionar_placeholder(
        campo_senha,
        "  Crie uma senha",
        senha=True
    )

# ─────────────────── Confirmar senha ───────────────────

    campo_confirmar_senha = Entry(
        frame_principal,
        font=("Arial", 12),
        fg="#172633",
        bg="white",
        relief="solid",
        bd=1
    )

    campo_confirmar_senha.grid(
        row=5,
        column=0,
        padx=25,
        pady=(0, 18),
        sticky="ew",
        ipady=9
    )

    adicionar_placeholder(
        campo_confirmar_senha,
        "  Confirme sua senha",
        senha=True
    )

# ─────────────────── Criar conta ───────────────────

    def criar_conta():

        nome = campo_nome.get().strip()
        email = campo_email.get().strip()
        senha = campo_senha.get()
        confirmar_senha = campo_confirmar_senha.get()

        # Impedir que os placeholders sejam enviados
        if (nome in ("", "  Nome completo")
            or email in ("", "  E-mail")
            or senha in ("", "  Crie uma senha")
            or confirmar_senha in ("", "  Confirme sua senha")
        ):
            print("Preencha todos os campos.")
            return

        if senha != confirmar_senha:
            print("As senhas não coincidem.")
            return

        print("Dados preenchidos corretamente!")
        print("Próximo passo: cadastrar no banco de dados.")

# ─────────────────── Botão criar conta ───────────────────



    botao_criar = Button(
        frame_principal,
        text="Criar conta  →",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#172027",
        activebackground="#293944",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=criar_conta
    )

    botao_criar.grid(
        row=6,
        column=0,
        padx=25,
        pady=(0, 10),
        sticky="ew",
        ipady=8
    )

# ─────────────────── Área inferior ───────────────────

    frame_login = Frame(
        frame_principal,
        bg="#F1EFEF"
    )

    frame_login.grid(
        row=8,
        column=0,
        pady=(0, 22)
    )

    texto_login = Label(
        frame_login,
        text="Já tem uma conta?",
        font=("Arial", 9),
        fg="#697786",
        bg="#F1EFEF"
    )

    texto_login.grid(
        row=0,
        column=0
    )

 # ─────────────────── Link - Login <-- Criar conta ───────────────────

    from GUI_conexões.criar_conta__entrar import voltar_login

    link_login = Label(
        frame_login,
        text="Entrar",
        font=("Arial", 9, "underline"),
        fg="#172633",
        bg="#F1EFEF",
        cursor="hand2"
    )

    link_login.grid(
        row=0,
        column=1,
        padx=(5, 0)
    )

    link_login.bind(
        "<Button-1>",
        lambda event: voltar_login(event, janela))























if __name__ == "__main__":
    janela = Tk()
    executar_gui_cadastro(janela)
    janela.mainloop()