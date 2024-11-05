class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
    
    def salvar_venda_em_json(self, caminho_arquivo='vendas.json'):
        venda_data = {
            "dataVenda": self.__dataVenda,
            "produtos": [{
                "nome": produto.get_nome(),
                "preco": produto.get_preco(),
                "quantidade": produto.get_quantidade()
            } for produto in self.__produtos],
            "total": self.get_total()
        }

        try:
            with open(caminho_arquivo, 'r') as file:
                vendas = json.load(file)
        except FileNotFoundError:
            vendas = []

        vendas.append(venda_data)

        with open(caminho_arquivo, 'w') as file:
            json.dump(vendas, file, indent=4)