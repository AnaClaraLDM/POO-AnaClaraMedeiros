from ContaBancaria import ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self,titular,cpf,saldo,numerocc):
        super().__init__(titular,cpf,saldo)
        self.numerocc = numerocc
   
    def mostrar_cc(self):
        return (f"\n***********************\nTitular da conta:{self.titular}\n CPF do titular: {self.cpf}\n Número da conta: {self.numerocc}\n Saldo da conta: {self.saldo:.2f}\n***********************\n")