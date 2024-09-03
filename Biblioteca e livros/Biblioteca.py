from Livro import Livro
class Biblioteca:
    def __init__(self):
        self.__livros = []
    
    def adicionarLivro(self, livros):
        self.__livros.append(livros)  

    def buscarLivro(self, nome):
        for livro in self.__livros:
            if livro.getNome().lower() == nome.lower():
                return livro 
        return None 

    def removerLivro(self, nome):
        livro = self.buscarLivro(nome)
        if livro:
            self.__livros.remove(livro)  
            return True
        return False  

    def listarLivros(self):
        if not self.__livros:
            print("Este livro não existe nessa biblioteca")
        else:
            for livros in self.__livros:
                livros.exibirLivro()

    