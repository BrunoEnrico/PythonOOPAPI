import json

from app import App
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



def main():
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    """     restaurante_praca = Restaurante('praça', 'Gourmet')
    bebida_suco = Bebida('Melancia', 3.50, tamanho="Grande")
    prato_salada = Prato('Salada', 15.99, descricao="Muito bom")
    bebida_suco.aplicar_desconto()
    prato_salada.aplicar_desconto()
    restaurante_praca.adicionar_ao_cardapio(bebida_suco)
    restaurante_praca.adicionar_ao_cardapio(prato_salada)

    restaurante_praca.receber_avaliacao('Gui', 10)
    restaurante_praca.receber_avaliacao('Lais', 8)
    restaurante_praca.receber_avaliacao('Emy', 2)
    restaurante_praca.exibir_cardapio() """

    app = App()
    response = app.get_request_response(url)

    response_dict = app.convert_json_response_to_dict(response, "Company", ["Item", "price", "description"])
    for nome_restaurante, dados in response_dict.items():
        filename = f"{nome_restaurante}.json"

        with open(filename, "w") as file:
            json.dump(dados, file, indent=4)

if __name__ == '__main__':
    main()