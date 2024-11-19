from tkinter import *

janela = Tk()

titulo = Label(janela,text="Interface Gráfica", justify="left")
titulo.grid(row=0, column=0)
titulo["font"] = ("inter", "28", "bold")
titulo["fg"] = "purple"

subtitulo = "Em python com tkinter"
frase1 = Label(janela, text = subtitulo, justify="left")
frase1.grid(row=1, column=0)
frase1["font"] = ("inter", "16")
frase1["fg"] = ("gray")

img = PhotoImage(file = "carro.png")
imagem = Label(janela, image = img)
imagem.grid(row=2,column=0)

conteudo = """A Interface Gráfica do Usuário
(GUI – Graphic User Interface) é
uma forma de exibição que permite
representar os itens interativos de
um programa através de elementos
gráficos como: botões, caixas de
seleção, campos de digitação, etc."""
frase2 = Label(janela, text = conteudo, justify="center")
frase2.grid(row=3, column=0)
frase2["font"] = ("inter", "14")
frase2["fg"] = ("black")

botao_sair = Button(janela)
botao_sair.grid(row=4, column=4)
botao_sair["text"] = "Sair de 'praticando.py'"
botao_sair["font"] = ("inter", "10")
botao_sair["width"] = 20
botao_sair["command"] = quit

janela.mainloop()