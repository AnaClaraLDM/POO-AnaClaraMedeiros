from ContaBancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self,titular,cpf,saldo,rendimento):
        super().__init__(titular,cpf,saldo)
        self.rendimento = rendimento
   
    def ver_rendimento(self):
        return self.rendimento*self.saldo


    def render(self):
        self.saldo += self.saldo*self.rendimento
