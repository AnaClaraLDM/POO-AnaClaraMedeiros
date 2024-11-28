from json import *
from Produto import Produto
from Venda import Venda

data = input("Digite a data da venda (formato: DD/MM/AAAA): ")
venda = Venda(data)
opcao = "0"

while opcao != "6":
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos e Mostrar Total")
    print("4. Salvar em arquivo")
    print("5. Incorporar dados json")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ")

        preco_valido = False
        while not preco_valido:
            preco = input("Preço do Produto: ")
            preco = preco.replace(',', '.')
            pontos = 0
            for caractere in preco:
                if caractere == '.':
                    pontos += 1
            if pontos <= 1:
                partes = preco.split('.')
                valido = True
                for parte in partes:
                    if not parte.isdigit() and parte != '':
                        valido = False
                        break
                if valido:
                    preco = float(preco)
                    preco_valido = True
                else:
                    print("Preço inválido. Por favor, insira um valor numérico.")
            else:
                print("Preço inválido. Por favor, insira um valor numérico.")

        quantidade_valida = False
        while not quantidade_valida:
            quantidade = input("Quantidade em Estoque: ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                quantidade_valida = True
            else:
                print("Quantidade inválida. Por favor, insira um número inteiro.")

        produto = Produto(nome, preco, quantidade)
        venda.get_produtos().append(produto)

    elif opcao == "2":
        nome = input("Nome do Produto a remover: ")
        venda.removerProduto(nome)

    elif opcao == "3":
        venda.listarProdutos()
        print(f"Total da Venda: R${venda.calcularTotal():.2f}")

    elif opcao == "4":
        arquivo = input("Digite o nome do arquivo: ")
        venda.salvarEmJson(arquivo)

    elif opcao == "5":
        arquivo = input("Nome do arquivo com os dados dos livros: ")
        venda.recuperarDeJson(arquivo)      

    elif opcao == "6":
        print("Saindo...")

    else:
        print("Opção inválida, tente novamente.")