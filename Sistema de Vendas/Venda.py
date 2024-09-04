class Venda:
    def __init__(self, produtos, dataVenda):
        self.produtos = produtos
        self.dataVenda = dataVenda
        self.total = 0.0

    def get_produtos(self):
        return self.produtos

    def get_dataVenda(self):
        return self.dataVenda

    def get_total(self):
        return self.total

    def set_produtos(self, produtos):
        self.produtos = produtos

    def set_dataVenda(self, dataVenda):
        self.dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def removerProduto(self, nome):
        for produto in self.produtos:
            if produto.get_nome() == nome:
                self.produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.produtos:
            print("Nenhum produto na venda.")
        else:
            print("\nProdutos na Venda:")
            for produto in self.produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
