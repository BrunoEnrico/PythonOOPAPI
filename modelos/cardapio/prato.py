from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str) -> None:
        super().__init__(nome=nome, preco=preco)
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def __str__(self):
        return self._nome

        