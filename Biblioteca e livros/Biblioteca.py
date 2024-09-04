class Biblioteca:
    def __init__(self):
        self._livros = []

    def adicionarLivro(self, livro):
        self._livros.append(livro)
        print(f"Livro '{livro.get_titulo()}' adicionado com sucesso!")

    def removerLivro(self, titulo):
        for livro in self._livros:
            if livro.get_titulo() == titulo:
                self._livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def buscarLivro(self, titulo):
        for livro in self._livros:
            if livro.get_titulo() == titulo:
                print(f"Livro encontrado: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano: {livro.get_anoPublicacao()}")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def listarLivros(self):
        if not self._livros:
            print("Nenhum livro disponível na biblioteca.")
        else:
            print("Lista de Livros na Biblioteca:")
            for livro in self._livros:
                print(f"- {livro.get_titulo()} ({livro.get_anoPublicacao()}), Autor: {livro.get_autor().get_nome()}")
