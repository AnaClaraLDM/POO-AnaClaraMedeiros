from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Somador") 
janela.geometry("200x300")
janela.resizable(False, True) 

rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)

rotulo_resultado = Label(janela, text="Resultado:")
rotulo_resultado.grid(row=3, column=0)

campo_resultado = Entry(janela, text="Resultado", state="readonly")
campo_resultado.grid(row=3, column=1)


def somar():
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        soma = v1+v2
        print(soma)
        campo_resultado.config(state="normal")
        campo_resultado.delete(0,END)
        campo_resultado.insert(0,soma)
        campo_resultado.config(state="readonly")
    except ValueError:
        messagebox.showerror("Erro","insira valores válidos")

def subtrair():
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        subtrair = v1-v2
        campo_resultado.config(state="normal")
        campo_resultado.delete(0,END)
        campo_resultado.insert(0,subtrair)
        campo_resultado.config(state="readonly")
    except ValueError:
        messagebox.showerror("Erro","insira valores válidos")

def multiplicar():
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        multiplicar = v1*v2
        campo_resultado.config(state="normal")
        campo_resultado.delete(0,END)
        campo_resultado.insert(0,multiplicar)
        campo_resultado.config(state="readonly")
        campo_resultado["state"] = "disabled"
    except ValueError:
        messagebox.showerror("Erro","insira valores válidos")

def dividir():
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        dividir = v1/v2
        campo_resultado.config(state="normal")
        campo_resultado.delete(0,END)
        campo_resultado.insert(0,dividir)
        campo_resultado.config(state="readonly")
    except ValueError:
        messagebox.showerror("Erro","insira valores válidos")



botao1 = Button(janela, text = "Somar")
botao1.grid(row=4,column=1)
botao1["width"] = 15
botao1["command"] = somar

botao2 = Button(janela, text = "Subtrair")
botao2.grid(row=5,column=1)
botao2["width"] = 15
botao2["command"] = subtrair

botao3 = Button(janela, text = "Multiplicar")
botao3.grid(row=6,column=1)
botao3["width"] = 15
botao3["command"] = multiplicar

botao4 = Button(janela, text = "Dividir")
botao4.grid(row=7,column=1)
botao4["width"] = 15
botao4["command"] = dividir

botao_sair = Button(janela)
botao_sair.grid(row=8, column=1)
botao_sair["text"] = "Sair"
botao_sair["width"] = 15
botao_sair["command"] = quit

janela.mainloop()
