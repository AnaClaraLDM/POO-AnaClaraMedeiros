from Biblioteca import Biblioteca
from Livro import Livro
from Autor import Autor

biblioteca = Biblioteca()
opcao = "0"

while opcao != "5":
    print("\nMenu:")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro")
    print("4. Listar Livros")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do Livro: ")
        nome_autor = input("Nome do Autor: ")
        nacionalidade = input("Nacionalidade do Autor: ")
        data_nascimento = input("Data de Nascimento do Autor: ")
        
        ano_publicacao = input("Ano de Publicação: ")
        while not ano_publicacao.isdigit():
            print("Ano de Publicação inválido. Por favor, insira um número inteiro.")
            ano_publicacao = input("Ano de Publicação: ")
        ano_publicacao = int(ano_publicacao)

        autor = Autor(nome_autor, nacionalidade, data_nascimento)
        livro = Livro(titulo, autor, ano_publicacao)
        biblioteca.adicionarLivro(livro)

    elif opcao == "2":
        titulo = input("Título do Livro a remover: ")
        biblioteca.removerLivro(titulo)

    elif opcao == "3":
        titulo = input("Título do Livro a buscar: ")
        biblioteca.buscarLivro(titulo)

    elif opcao == "4":
        biblioteca.listarLivros()

    elif opcao == "5":
        print("Saindo...")

    else:
        print("Opção inválida, tente novamente.")