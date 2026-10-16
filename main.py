import tkinter as tk
import importlib
import threading
import time
import os

# ─────────────────── Gui Home ───────────────────

'''import GUI.Área_do_cliente.gui_home as gui_home


root = tk.Tk()

root.geometry("900x600")

#root.resizable(False, False)
root.title("F22 - EXPRESS")


def carregar_interface():

    global gui_home

    try:

        importlib.reload(gui_home)

        for widget in root.winfo_children():
            widget.destroy()

        gui_home.executar_janela_home(root)

    except Exception as erro:

        print("Erro ao atualizar:")
        print(erro)


def observar_arquivo():

    arquivo = "GUI/Área_do_cliente/gui_home.py"

    ultima_modificacao = os.path.getmtime(arquivo)

    while True:

        time.sleep(0.5)

        nova_modificacao = os.path.getmtime(arquivo)

        if nova_modificacao != ultima_modificacao:

            ultima_modificacao = nova_modificacao

            root.after(0, carregar_interface)


threading.Thread(
    target=observar_arquivo,
    daemon=True
).start()


carregar_interface()

root.mainloop()





# ─────────────────── Meus dados ───────────────────

import GUI.Área_do_cliente.meus_dados as meus_dados


root = tk.Tk()

#root.geometry("1000x1000")

#root.resizable(False, False)
root.title("F22 - EXPRESS")


def carregar_interface():

    global meus_dados

    try:

        importlib.reload(meus_dados)

        for widget in root.winfo_children():
            widget.destroy()

        meus_dados.executar_janela_login(root)

    except Exception as erro:

        print("Erro ao atualizar:")
        print(erro)


def observar_arquivo():

    arquivo = "GUI/Área_do_cliente/meus_dados.py"

    ultima_modificacao = os.path.getmtime(arquivo)

    while True:

        time.sleep(0.5)

        nova_modificacao = os.path.getmtime(arquivo)

        if nova_modificacao != ultima_modificacao:

            ultima_modificacao = nova_modificacao

            root.after(0, carregar_interface)


threading.Thread(
    target=observar_arquivo,
    daemon=True
).start()


carregar_interface()

root.mainloop()



# ─────────────────── Consultar Voos ───────────────────

import GUI.Área_do_cliente.consultar_voos as consultar_voos


root = tk.Tk()

root.geometry("900x600")

#root.resizable(False, False)
root.title("F22 - EXPRESS")


def carregar_interface():

    global consultar_voos

    try:

        importlib.reload(consultar_voos)

        for widget in root.winfo_children():
            widget.destroy()

        consultar_voos.executar_janela_consultar_voos(root)

    except Exception as erro:

        print("Erro ao atualizar:")
        print(erro)


def observar_arquivo():

    arquivo = "GUI/Área_do_cliente/consultar_voos.py"

    ultima_modificacao = os.path.getmtime(arquivo)

    while True:

        time.sleep(0.5)

        nova_modificacao = os.path.getmtime(arquivo)

        if nova_modificacao != ultima_modificacao:

            ultima_modificacao = nova_modificacao

            root.after(0, carregar_interface)


threading.Thread(
    target=observar_arquivo,
    daemon=True
).start()


carregar_interface()

root.mainloop()

'''

# ─────────────────── Gui Login ───────────────────

import GUI.Área_login.entrar as gui_login


root = tk.Tk()

#root.geometry("900x600")

#root.resizable(False, False)
root.title("F22 - EXPRESS")


def carregar_interface():

    global gui_login

    try:

        importlib.reload(gui_login)

        for widget in root.winfo_children():
            widget.destroy()

        gui_login.executar_gui_login(root)

    except Exception as erro:

        print("Erro ao atualizar:")
        print(erro)


def observar_arquivo():

    arquivo = "GUI/Área_login/entrar.py"

    ultima_modificacao = os.path.getmtime(arquivo)

    while True:

        time.sleep(0.5)

        nova_modificacao = os.path.getmtime(arquivo)

        if nova_modificacao != ultima_modificacao:

            ultima_modificacao = nova_modificacao

            root.after(0, carregar_interface)


threading.Thread(
    target=observar_arquivo,
    daemon=True
).start()


carregar_interface()

root.mainloop()