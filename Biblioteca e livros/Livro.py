class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor

    def get_anoPublicacao(self):
        return self._anoPublicacao

    def set_anoPublicacao(self, anoPublicacao):
        self._anoPublicacao = anoPublicacao
