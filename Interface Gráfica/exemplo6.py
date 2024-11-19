from tkinter import *
janela = Tk()

rotulo = Label(janela,text="Olá!Mundo")
rotulo.grid(row=0, column=0)
botao_sair = Button(janela)
botao_sair.grid(row=1, column=1)
botao_sair["text"] = "Sair"
botao_sair["width"] = 10
botao_sair["command"] = quit

janela.mainloop()