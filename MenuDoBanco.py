from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

lista_de_contas = []

opcao = 0

while opcao != 8:
    # Menu principal
    print("*** Bem Vindo ao Banco Central ***")
    print("1) Abrir uma nova conta")
    print("2) Listar contas")
    print("3) Depositar")
    print("4) Sacar")
    print("5) Mostrar Conta")
    print("6) Verificar Saldo")
    print("7) Acessar conta")
    print("8) SAIR")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        titular = input("Informe o nome do titular: ")
        cpf = input("Informe o CPF do titular: ") 
        saldo = float(input("Informe o saldo inicial: "))
        tipo = int(input("Informe o tipo de Conta: 1) Poupança 2) Corrente \n"))

        if tipo == 1:
            rendimento = float(input("Informe o rendimento mensal da conta: "))
            conta = ContaPoupanca(titular, cpf, saldo, rendimento)
            lista_de_contas.append(conta)
            print(f"Conta Poupança criada com sucesso para {titular}!")

            rendimento_aplicado = False

            opcao_poupanca = 0
            while opcao_poupanca != 3:
                print(f"*** Bem vindo(a) {titular} ***")
                print("1) Render")
                print("2) Ver rendimento")
                print("3) Voltar ao menu principal")
                opcao_poupanca = int(input("Digite a sua opção: "))

                if opcao_poupanca == 1:
                    if not rendimento_aplicado:
                        conta.render()
                        rendimento_aplicado = True  
                    else:
                        print("O rendimento já foi aplicado e não pode ser acionado novamente.")
                elif opcao_poupanca == 2:
                    if rendimento_aplicado:
                        print(f"O rendimento aplicado é de: {conta.ver_rendimento():.2f}")
                    else:
                        print(f"O rendimento potencial é de: {conta.ver_rendimento():.2f}")
                elif opcao_poupanca == 3:
                    print("Voltando ao menu principal...")
                else:
                    print("Opção inválida. Tente novamente.")

        elif tipo == 2:
            numerocc = input("Informe o número da conta: ")
            conta = ContaCorrente(titular, cpf, saldo, numerocc)
            lista_de_contas.append(conta)
            print(f"Conta Corrente criada com sucesso para {titular}!")

            opcao_corrente = 0
            while opcao_corrente != 2:
                print(f"*** Bem vindo(a) {titular} ***")
                print("1) Mostrar detalhes da conta corrente")
                print("2) Voltar ao menu principal")
                opcao_corrente = int(input("Digite a sua opção: "))

                if opcao_corrente == 1:
                    print(conta.mostrar_cc())  
                elif opcao_corrente == 2:
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        else:
            print("Tipo de conta inválido")

    elif opcao == 2:
        if not lista_de_contas:
            print("Nenhuma conta cadastrada.")
        else:
            for conta in lista_de_contas:
                print(conta.mostrar_conta())

    elif opcao == 3:
        if not lista_de_contas:
            print("Nenhuma conta cadastrada.")
        else:
            cpf_deposito = input("Informe o CPF do titular da conta para depósito: ")
            valor = float(input("Informe o valor do depósito: "))
            for conta in lista_de_contas:
                if conta.cpf == cpf_deposito:
                    conta.depositar(valor)
                    print(f"Depósito de R${valor} realizado com sucesso para {conta.titular}!")
                    break
            else:
                print("Conta não encontrada.")

    elif opcao == 4:
        if not lista_de_contas:
            print("Nenhuma conta cadastrada.")
        else:
            cpf_saque = input("Informe o CPF do titular da conta para saque: ")
            valor = float(input("Informe o valor do saque: "))
            conta_encontrada = False
            for conta in lista_de_contas:
                if conta.cpf == cpf_saque:
                    resultado = conta.sacar(valor)
                    print(f"Saque de R${valor} realizado com sucesso para {conta.titular}!")
                    if resultado is not None:
                        print(resultado)
                    conta_encontrada = True
                    break
            if not conta_encontrada:
                print("Conta não encontrada.")

    elif opcao == 5:
        if not lista_de_contas:
            print("Nenhuma conta cadastrada.")
        else:
            cpf_mostrar = input("Informe o CPF do titular da conta para mostrar os detalhes: ")
            for conta in lista_de_contas:
                if conta.cpf == cpf_mostrar:
                    print(conta.mostrar_conta())
                    break
            else:
                print("Conta não encontrada.")
    elif opcao == 6:
        if not lista_de_contas:
            print("Nenhuma conta cadastrada.")
        else:
            cpf_verificar = input("Informe o CPF do titular da conta: ")
            conta_encontrada = False
            for conta in lista_de_contas:
                if conta.cpf == cpf_verificar:
                    print(f"Saldo atual: R${conta.saldo:.2f}")
                    conta_encontrada = True
                    break
        
            if not conta_encontrada:
                print("Conta não encontrada.")
    elif opcao == 7:  
        cpf_acesso = input("Informe o CPF do titular da conta que deseja acessar: ")
        for conta in lista_de_contas:
            if conta.cpf == cpf_acesso:
                if isinstance(conta, ContaPoupanca):
                    opcao_poupanca = 0
                    while opcao_poupanca != 3:
                        print(f"*** Bem vindo(a) {conta.titular} ***")
                        print("1) Render")
                        print("2) Ver rendimento")
                        print("3) Voltar ao menu principal")
                        opcao_poupanca = int(input("Digite a sua opção: "))

                        if opcao_poupanca == 1:
                            if not rendimento_aplicado:
                                conta.render()
                                rendimento_aplicado = True
                            else:
                                print("O rendimento já foi aplicado e não pode ser acionado novamente.")
                        elif opcao_poupanca == 2:
                            if rendimento_aplicado:
                                print(f"O rendimento aplicado é de: {conta.ver_rendimento():.2f}")
                            else:
                                print(f"O rendimento potencial é de: {conta.ver_rendimento():.2f}")
                        elif opcao_poupanca == 3:
                            print("Voltando ao menu principal...")
                        else:
                            print("Opção inválida. Tente novamente.")
                elif isinstance(conta, ContaCorrente):
                    opcao_corrente = 0
                    while opcao_corrente != 2:
                        print(f"*** Bem vindo(a) {conta.titular} ***")
                        print("1) Mostrar detalhes da conta corrente")
                        print("2) Voltar ao menu principal")
                        opcao_corrente = int(input("Digite a sua opção: "))

                        if opcao_corrente == 1:
                            print(conta.mostrar_cc())
                        elif opcao_corrente == 2:
                            print("Voltando ao menu principal...")
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                break
        else:
            print("Conta não encontrada.")
    elif opcao == 8:
        print("Encerrando o sistema...")
    else:
        print("Opção inválida. Tente novamente.")
