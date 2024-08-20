class ContaBancaria:
    def __init__(self,titular,cpf,saldo):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
   
    def mostrar_conta(self):
        return (f"\nTitular da conta:{self.titular}\n CPF do titular: {self.cpf}\n Saldo da conta: {self.saldo:.2f}\n")


    def depositar(self,adicao):
        self.saldo  = self.saldo + adicao


    def sacar(self,subtrair):
        if(self.saldo >= subtrair):
            self.saldo = self.saldo - subtrair
        else:
            return (f"\nO valor do saque é maior que o saldo da sua conta")


    def verificar_saldo(self):
        return (f"\nSaldo da conta: {self.saldo:.2f}")