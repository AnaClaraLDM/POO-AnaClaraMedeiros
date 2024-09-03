from Biblioteca import Biblioteca
from Livro import Livro
from Autor import Autor

opcao = 0

biblioteca = Biblioteca()

while opcao!= 5:
    print("-----------Menu da Biblioteca-----------")
    print("1) Adicionar um novo livro  à biblioteca")
    print("2) Remover um livro")
    print("3) Buscar um livro")
    print("4) Listar todos os livros disponíveis")
    print("5) Sair da biblioteca")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        nome = input("\nQual o nome do autor do livro: ")
        nacionalidade = input("\nQual a nacinalidade do autor do livro: ")
        dataNascimento = input("\nQual a data de nascimento do autor do livro: ")
        titulo = input("\nQual o título do livro: ")
        anoPublicacao = input("\nQual o ano de publicação do livro: ")
        autor = Autor(nome,nacionalidade,dataNascimento)
        livro = Livro(titulo,autor,anoPublicacao)
        biblioteca.adicionarLivro(livro)
    
    elif opcao == 2:
        titulo = input("\nQual o título do livro que você deseja excluir? ")
        biblioteca.removerLivro(titulo)
    
    elif opcao == 3:
        titulo = input("\nQual o título do livro que você deseja achar? ")
        livro  = biblioteca.buscarLivro(titulo)
        if livro livros = []:
        livro.exibirLivro()
    
    elif opcao == 4:
        biblioteca.listarLivros()
    
    elif opcao == 5:
        print("Encerrando o sistema...")

    else:
        print("Opção inválida. Tente novamente.")
    

        
        





