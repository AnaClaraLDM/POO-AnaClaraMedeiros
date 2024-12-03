from Biblioteca import Biblioteca
from tkinter import *

biblioteca = Biblioteca()
janela = Tk()
janela.title("Sistema de Biblioteca")
# Widgets
Label(janela, text="Título do Livro:").grid(row=0, column=0, sticky="w")
input_titulo = Entry(janela, width=30)
input_titulo.grid(row=0, column=1)

Label(janela, text="Nome do Autor:").grid(row=1, column=0, sticky="w")
input_autor = Entry(janela, width=30)
input_autor.grid(row=1, column=1)

Label(janela, text="Nacionalidade do Autor:").grid(row=2, column=0, sticky="w")
input_nacionalidade = Entry(janela, width=30)
input_nacionalidade.grid(row=2, column=1)

Label(janela, text="Data de Nascimento do Autor:").grid(row=3, column=0, sticky="w")
input_data_nascimento = Entry(janela, width=30)
input_data_nascimento.grid(row=3, column=1)

Label(janela, text="Ano de Publicação:").grid(row=4, column=0, sticky="w")
input_ano_publicacao = Entry(janela, width=30)
input_ano_publicacao.grid(row=4, column=1)

Button(janela, text="Adicionar Livro", command=biblioteca.adicionarLivro).grid(row=5, column=0, pady=5)
Button(janela, text="Remover Livro", command=biblioteca.removerLivro).grid(row=5, column=1, pady=5)
Button(janela, text="Buscar Livro", command=biblioteca.buscarLivro).grid(row=6, column=0, pady=5)
Button(janela, text="Listar Livros", command=biblioteca.listarLivros).grid(row=6, column=1, pady=5)

Button(janela, text="Sair", command=janela.quit).grid(row=7, column=0, columnspan=2, pady=10)
janela.mainloop()
