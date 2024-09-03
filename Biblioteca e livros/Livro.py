class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao
    
    def getNome(self):
        return self.__titulo
    
    def setNome(self,titulo):
        self.__titulo = titulo
    
    def getNome(self):
        return self.__autor
    
    def setNome(self,autor):
        self.__autor = autor
    
    def getNome(self):
        return self.__anoPublicacao
    
    def setNome(self,anoPublicacao):
<<<<<<< HEAD
        self.__anoPublicacao = anoPublicacao
    
    def exibirLivro(self):
        print(f"Título: {self.__titulo}")
        print(f"Ano de publicação: {self.__anoPublicacao}")
        self.__autor.exibirAutor()
=======
        self.__anoPublicacao = anoPublicacao
>>>>>>> origin/main
