class Produto:

    def __init__(self,nome,preco,quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    def getNome(self):
        return self.__nome
    
    def setNome(self,nome):
        self.__nome = nome

    def getPreco(self):
        return self.__idade
    
    def setPreco(self,preco):
        if preco > 0:
            self.__preco = preco
        else:
            print(preco," é um valor inválido")

    def getQuantidade(self):
        return self.__quantidade
    
    def setQuantidade(self,quantidade):
        if quantidade >= 0 and quantidade.is_integer():
            self.__quantidade = quantidade