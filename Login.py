import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")
janela.resizable(True, True)


rotulo_usuario = tk.Label(janela, text="Usuário:")
rotulo_usuario.pack()
campo_usuario = tk.Entry(janela)
campo_usuario.pack()

rotulo_senha = tk.Label(janela, text="Senha:")
rotulo_senha.pack()
campo_senha = tk.Entry(janela, show="*") 
campo_senha.pack()

def entrar():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "user" and senha == "123":
        messagebox.showinfo("Sucesso", "Acesso permitido!")
    else:
        messagebox.showerror("Erro", "Acesso negado.")

botao_entrar = tk.Button(janela, text="Entrar", command=entrar)
botao_entrar.pack()

janela.mainloop()