from Livro import Livro
class Biblioteca:
    def __init__(self):
        self.__livros = []
    
    def adicionarLivro(self, livros):
        self.__livros.append(livros)  

    def buscarLivro(self, nome):
<<<<<<< HEAD
        for livro in self.__livros:
            if livro.getNome().lower() == nome.lower():
                return livro 
            else:
                return("Livro não encontrado")
=======
        for livros in self.__livros:
            if livros.getNome().lower() == nome.lower():
                return livros  
        return None 
>>>>>>> origin/main

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
<<<<<<< HEAD
                livros.exibirLivro()

    
=======
                livros.exibirLivro()
>>>>>>> origin/main
