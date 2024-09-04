class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self._nome = nome
        self._nacionalidade = nacionalidade
        self._dataNascimento = dataNascimento

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_nacionalidade(self):
        return self._nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self._nacionalidade = nacionalidade

    def get_dataNascimento(self):
        return self._dataNascimento

    def set_dataNascimento(self, dataNascimento):
        self._dataNascimento = dataNascimento

    def exibirAutor(self):
        print(f"Autor: {self._nome}, Nacionalidade: {self._nacionalidade}, Data de Nascimento: {self._dataNascimento}")
