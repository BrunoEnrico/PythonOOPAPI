from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: str) -> None:
        super().__init__(nome=nome, preco=preco)
        self._tamanho = tamanho