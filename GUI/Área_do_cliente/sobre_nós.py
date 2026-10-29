from tkinter import *
from tkinter import ttk


def executar_janela_sobre_nos(janela_sobre):

    for widget in janela_sobre.winfo_children():
        widget.destroy()

    # ─────────────────── Configuração ───────────────────

    AZUL = "#172B3A"
    AZUL_CLARO = "#2878A5"
    FUNDO = "#F4F6F8"
    TEXTO = "#344454"
    CINZA = "#718096"
    LINHA = "#DCE3E9"
    BRANCO = "#FFFFFF"

    janela_sobre.title("F22 - EXPRESS | Sobre Nós")
    #janela_sobre.geometry("700x600")
    janela_sobre.configure(bg=FUNDO)

    janela_sobre.columnconfigure(0, weight=1)
    janela_sobre.rowconfigure(1, weight=1)

    # ─────────────────── Cabeçalho ───────────────────

    topo = Frame(janela_sobre, bg=AZUL, height=70)
    topo.grid(row=0, column=0, sticky="ew")
    topo.grid_propagate(False)
    topo.columnconfigure(0, weight=1)

    Label(
        topo,
        text="✈  F22 - EXPRESS",
        font=("Ubuntu", 17, "bold"),
        fg=BRANCO,
        bg=AZUL
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=30,
        pady=18
    )

    Label(
        topo,
        text="INSTITUCIONAL",
        font=("Arial", 9, "bold"),
        fg="#B8D5E8",
        bg=AZUL
    ).grid(
        row=0,
        column=1,
        padx=30
    )

    # ─────────────────── Área rolável ───────────────────

    area = Frame(janela_sobre, bg=FUNDO)
    area.grid(row=1, column=0, sticky="nsew")

    area.columnconfigure(0, weight=1)
    area.rowconfigure(0, weight=1)

    canvas = Canvas(
        area,
        bg=FUNDO,
        highlightthickness=0,
        bd=0
    )
    canvas.grid(row=0, column=0, sticky="nsew")

    barra = ttk.Scrollbar(
        area,
        orient="vertical",
        command=canvas.yview
    )
    barra.grid(row=0, column=1, sticky="ns")

    canvas.configure(yscrollcommand=barra.set)

    documento = Frame(canvas, bg=FUNDO)

    id_documento = canvas.create_window(
        (0, 0),
        window=documento,
        anchor="nw"
    )

    documento.columnconfigure(0, weight=1)

    def atualizar_rolagem(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def ajustar_largura(event):
        canvas.itemconfigure(id_documento, width=event.width)

    documento.bind("<Configure>", atualizar_rolagem)
    canvas.bind("<Configure>", ajustar_largura)

    # ─────────────────── Conteúdo do documento ───────────────────

    conteudo = Frame(
        documento,
        bg="red",
        padx=30,
        pady=28
    )

    conteudo.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=24,
        pady=24
    )

    conteudo.columnconfigure(0, weight=1)

    linha_atual = 0

    # Linha de destaque superior
    Frame(
        conteudo,
        bg=AZUL_CLARO,
        height=4
    ).grid(
        row=linha_atual,
        column=0,
        sticky="ew",
        pady=(0, 22)
    )
    linha_atual += 1

    Label(
        conteudo,
        text="GUIA INSTITUCIONAL  /  APRESENTAÇÃO DO SISTEMA",
        font=("Arial", 8, "bold"),
        fg=AZUL_CLARO,
        bg=BRANCO
    ).grid(
        row=linha_atual,
        column=0,
        sticky="w",
        pady=(0, 10)
    )
    linha_atual += 1

    Label(
        conteudo,
        text="Conheça a F22 - EXPRESS",
        font=("Ubuntu", 25, "bold"),
        fg=AZUL,
        bg=BRANCO,
        wraplength=540,
        justify="left"
    ).grid(
        row=linha_atual,
        column=0,
        sticky="w",
        pady=(0, 8)
    )
    linha_atual += 1

    Label(
        conteudo,
        text=(
            "Uma apresentação do sistema, seus objetivos "
            "e os recursos preparados para o cliente."
        ),
        font=("Arial", 11),
        fg=CINZA,
        bg=BRANCO,
        wraplength=540,
        justify="left"
    ).grid(
        row=linha_atual,
        column=0,
        sticky="w",
        pady=(0, 20)
    )
    linha_atual += 1

    # Metadados
    metadados = Frame(
        conteudo,
        bg="#EEF3F7",
        padx=14,
        pady=12
    )
    metadados.grid(
        row=linha_atual,
        column=0,
        sticky="ew",
        pady=(0, 24)
    )
    linha_atual += 1

    Label(
        metadados,
        text="DOCUMENTO",
        font=("Arial", 8, "bold"),
        fg=CINZA,
        bg="#EEF3F7"
    ).grid(row=0, column=0, sticky="w")

    Label(
        metadados,
        text="Apresentação institucional",
        font=("Arial", 10, "bold"),
        fg=AZUL,
        bg="#EEF3F7"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=(4, 0)
    )

    # ─────────────────── Funções de formatação ───────────────────

    def secao(numero, titulo, texto):

        nonlocal linha_atual

        cabecalho = Frame(conteudo, bg=BRANCO)
        cabecalho.grid(
            row=linha_atual,
            column=0,
            sticky="ew",
            pady=(8, 8)
        )
        cabecalho.columnconfigure(1, weight=1)
        linha_atual += 1

        Label(
            cabecalho,
            text=numero,
            font=("Arial", 10, "bold"),
            fg=BRANCO,
            bg=AZUL,
            padx=9,
            pady=5
        ).grid(
            row=0,
            column=0,
            sticky="nw",
            padx=(0, 11)
        )

        Label(
            cabecalho,
            text=titulo,
            font=("Ubuntu", 14, "bold"),
            fg=AZUL,
            bg=BRANCO,
            wraplength=450,
            justify="left"
        ).grid(
            row=0,
            column=1,
            sticky="w",
            pady=3
        )

        Label(
            conteudo,
            text=texto,
            font=("Arial", 10),
            fg=TEXTO,
            bg=BRANCO,
            justify="left",
            anchor="w",
            wraplength=540
        ).grid(
            row=linha_atual,
            column=0,
            sticky="ew",
            pady=(0, 10)
        )
        linha_atual += 1

        Frame(
            conteudo,
            bg=LINHA,
            height=1
        ).grid(
            row=linha_atual,
            column=0,
            sticky="ew",
            pady=(3, 12)
        )
        linha_atual += 1

    def subtitulo(titulo, texto):

        nonlocal linha_atual

        Label(
            conteudo,
            text=titulo,
            font=("Arial", 11, "bold"),
            fg=AZUL,
            bg=BRANCO
        ).grid(
            row=linha_atual,
            column=0,
            sticky="w",
            pady=(3, 4)
        )
        linha_atual += 1

        Label(
            conteudo,
            text=texto,
            font=("Arial", 10),
            fg=TEXTO,
            bg=BRANCO,
            justify="left",
            anchor="w",
            wraplength=540
        ).grid(
            row=linha_atual,
            column=0,
            sticky="ew",
            pady=(0, 12)
        )
        linha_atual += 1

    # ─────────────────── Documentação ───────────────────

    secao(
        "01",
        "Apresentação",
        "A F22 - EXPRESS é um projeto de sistema desenvolvido "
        "com o propósito de reunir, em uma interface organizada, "
        "recursos relacionados à experiência de viagem do cliente. "
        "Sua proposta é oferecer um ambiente de navegação simples, "
        "no qual as principais opções possam ser localizadas "
        "com facilidade."
    )

    secao(
        "02",
        "Objetivo do sistema",
        "O objetivo é proporcionar uma experiência de utilização "
        "clara, intuitiva e organizada. A interface busca facilitar "
        "o acesso às áreas do sistema, manter uma apresentação "
        "consistente e permitir que o cliente compreenda a finalidade "
        "de cada opção disponível."
    )

    secao(
        "03",
        "Experiência do cliente",
        "A organização das telas foi pensada para orientar o usuário "
        "durante a navegação. Títulos, campos, botões e áreas de "
        "conteúdo possuem funções distintas, contribuindo para uma "
        "experiência visual mais compreensível e direta."
    )

    secao(
        "04",
        "Acesso à conta e cadastro",
        "A interface de acesso contém campos destinados ao e-mail "
        "e à senha, além de uma opção de continuidade com Google. "
        "O cadastro destina-se à entrada das informações necessárias "
        "para criar uma conta. A autenticação, o armazenamento seguro "
        "e a integração com serviços externos dependem da "
        "implementação técnica correspondente."
    )

    secao(
        "05",
        "Página inicial",
        "A página inicial funciona como ponto central de navegação. "
        "Ela apresenta a identidade do sistema e oferece atalhos "
        "para as áreas de consulta de voos, reservas e dados pessoais, "
        "permitindo que o cliente identifique rapidamente a seção "
        "que deseja acessar."
    )

    subtitulo(
        "Consulta de voos",
        "Área destinada à pesquisa de opções de viagem. Uma versão "
        "integrada poderá apresentar origem, destino, datas e "
        "informações sobre os voos encontrados. A consulta de voos "
        "reais depende de uma fonte de dados ou serviço apropriado."
    )

    subtitulo(
        "Minhas reservas",
        "Seção planejada para reunir informações referentes às "
        "reservas do cliente. A consulta de reservas efetivas exige "
        "um mecanismo de registro e acesso aos dados correspondentes."
    )

    subtitulo(
        "Meus dados",
        "Área destinada à visualização e, conforme os recursos "
        "implementados, à atualização das informações pessoais "
        "associadas à conta do cliente."
    )

    secao(
        "06",
        "Orientações de utilização",
        "Recomenda-se utilizar a página inicial como ponto de partida "
        "e selecionar a opção correspondente à necessidade. Para "
        "consultar viagens, acesse a área de voos; para localizar "
        "informações de reservas, utilize a seção de reservas; "
        "e, para consultar informações pessoais, acesse Meus Dados. "
        "As ações disponíveis variam conforme o estágio de "
        "desenvolvimento do sistema."
    )

    secao(
        "07",
        "Privacidade e proteção das informações",
        "Informações pessoais devem ser tratadas com cuidado. "
        "Uma versão operacional deve implementar controles de "
        "acesso e medidas adequadas de proteção dos dados. "
        "O cliente também deve evitar compartilhar suas credenciais. "
        "As medidas efetivamente aplicadas dependem da implementação "
        "e das políticas adotadas para o sistema."
    )

    secao(
        "08",
        "Escopo e evolução",
        "Esta documentação apresenta as finalidades previstas para "
        "as áreas da interface. A existência de uma tela ou botão "
        "não garante, por si só, que haja autenticação real, consulta "
        "de dados externos, armazenamento persistente ou confirmação "
        "de reservas. Cada recurso deve ser desenvolvido, integrado "
        "e testado antes de ser considerado operacional."
    )

    secao(
        "09",
        "Considerações finais",
        "A F22 - EXPRESS busca estabelecer uma base organizada "
        "para a navegação e o acesso a recursos relacionados "
        "à experiência de viagem. Sua estrutura permite desenvolver "
        "as funcionalidades gradualmente, mantendo o foco na clareza "
        "das informações, na consistência visual e na facilidade "
        "de utilização."
    )

    # ─────────────────── Encerramento ───────────────────

    Label(
        conteudo,
        text="F22 - EXPRESS",
        font=("Ubuntu", 15, "bold"),
        fg=AZUL,
        bg=BRANCO
    ).grid(
        row=linha_atual,
        column=0,
        sticky="w",
        pady=(8, 4)
    )
    linha_atual += 1

    Label(
        conteudo,
        text="Sua próxima viagem começa aqui.",
        font=("Arial", 10, "italic"),
        fg=CINZA,
        bg=BRANCO
    ).grid(
        row=linha_atual,
        column=0,
        sticky="w",
        pady=(0, 20)
    )

    # ─────────────────── Botão voltar ───────────────────

    from GUI_conexões.home__sobre_nos import voltar_botao

    botao_voltar = Button(
        conteudo,
        text="Sair",
        font=("Arial", 11, "bold"),
        fg="black",
        bg="white",
        command=lambda: voltar_botao(janela_sobre)
    )

    botao_voltar.grid(
        row=linha_atual,
        column=0,
        sticky="e",
        pady=(0, 20)
    )

    # ─────────────────── Rodapé fixo ───────────────────

    rodape = Frame(janela_sobre, bg=BRANCO)
    rodape.grid(row=2, column=0, sticky="ew")

    Frame(
        rodape,
        bg=LINHA,
        height=1
    ).pack(fill="x")

    Label(
        rodape,
        text="F22 - EXPRESS   •   DOCUMENTAÇÃO INSTITUCIONAL",
        font=("Arial", 8),
        fg=CINZA,
        bg=BRANCO
    ).pack(pady=10)

    # ─────────────────── Rolagem ───────────────────

    def rolar_mouse(event):
        canvas.yview_scroll(int(-event.delta / 120), "units")

    canvas.bind("<MouseWheel>", rolar_mouse)
    canvas.bind(
        "<Button-4>",
        lambda event: canvas.yview_scroll(-1, "units")
    )
    canvas.bind(
        "<Button-5>",
        lambda event: canvas.yview_scroll(1, "units")
    )


if __name__ == "__main__":
    janela = Tk()
    executar_janela_sobre_nos(janela)
    janela.mainloop()
