<<<<<<< HEAD
=======
from Data import Data

>>>>>>> origin/main
class Autor:
    def __init__(self,nome,nacionalidade,dataNascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento
    
    def getNome(self):
        return self.__nome
    
    def setNome(self,nome):
        self.__nome = nome
    
<<<<<<< HEAD
    def getNacionalidade(self):
        return self.__nacionalidade
    
    def setNacionalidade(self,nacionalidade):
        self.__nacionalidade = nacionalidade
    
    def getDataNascimento(self):
        return self.__dataNascimento
    
    def setDataNascimento(self,dataNascimento):
        self.__dataNascimento = dataNascimento
    
    def exibirAutor(self):
        print("Autor:")
        print(f"Nome: {self.__nome}")
        print(f"Nacionalidade: {self.__nacionalidade}")
        print(f"Data de nascimento: {self.__dataNascimento}")
=======
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
>>>>>>> origin/main
