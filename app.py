from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 3.50, tamanho="Grande")
prato_salada = Prato('Salada', 15.99, descricao="Muito bom")
restaurante_praca.adicionar_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_ao_cardapio(prato_salada)

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()