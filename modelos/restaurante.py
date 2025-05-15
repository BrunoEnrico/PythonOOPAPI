from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes: list['Restaurante'] = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao: list[Avaliacao] = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls: 'Restaurante'):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: int | float):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_ao_cardapio(self, item: ItemCardapio) -> None:
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self) -> None:
        print(f'Cardapio do restaurante: {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "_descricao"):
                mensagem_prato = f"""{i}. {item._nome} - R$ {item._preco} \n {item._descricao}"""
                print(mensagem_prato)
            else:
                mensagem_prato = f"""{i}. {item._nome} - R$ {item._preco} \n {item._tamanho}"""
                print(mensagem_prato)
