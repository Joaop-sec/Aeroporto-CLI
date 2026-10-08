from tkinter import *

janela = Tk()
janela.geometry("600x500")

janela.resizable(False, False)

titulo = Label(
    janela,
    text="F22 - EXPRESS",
    font=("Ubuntu", 20, "bold")
)
titulo.pack(pady=20)

texto = Label(
    janela,
    text="👤 Meus dados",
    font=("Ubuntu", 16, "bold")
)
texto.pack(pady=20)

campo_nome = Entry(
    janela,
    font=("Arial", 14)
)
campo_nome.pack(
    fill="x",
    padx=100,
    pady=10
)

campo_cpf = Entry(
    janela,
    font=("Arial", 14)
)
campo_cpf.pack(
    fill="x",
    padx=100,
    pady=10
)

campo_id = Entry(
    janela,
    font=("Arial", 14)
)
campo_id.pack(
    fill="x",
    padx=100,
    pady=10
)

botao = Button(
    janela,
    text="Editar dados",
    font=("Arial", 12)
)
botao.pack(pady=30)

janela.mainloop()