import tkinter as tk
import importlib
import threading
import time
import os

import GUI.Área_do_cliente.gui_home as gui_home


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