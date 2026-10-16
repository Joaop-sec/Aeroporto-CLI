# ─────────────────── Imports ───────────────────

from GUI.Área_login.criar_conta import executar_gui_cadastro

from GUI.Área_login.entrar import executar_gui_login

# ─────────────────── Entrar --> Criar conta ───────────────────

def abrir_cadastro(event, janela):
    executar_gui_cadastro(janela)


# ─────────────────── Link: Login <-- Criar conta ───────────────────

from GUI.Área_login.entrar import executar_gui_login


def voltar_login(event, janela):
    executar_gui_login(janela)
