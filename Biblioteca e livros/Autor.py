from Data import Data

class Autor:
    def __init__(self,nome,nacionalidade,dataNascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento
    
    def getNome(self):
        return self.__nome
    
    def setNome(self,nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nacionalidade
    
    def setNome(self,nacionalidade):
        self.__nacionalidade = nacionalidade
    
    def getNome(self):
        return self.__dataNascimento
    
    def setNome(self,dataNascimento):
        self.__dataNascimento = dataNascimento
    
    def exibirAutor(self):
        print(f"Nome: {self.__nome}")
        print(f"nacionalidade: {self.__nacionalidade}")
        print(self.__dataNascimento.getData())