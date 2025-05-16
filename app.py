from fastapi import FastAPI, Query
from request import Request

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    """
    Endpoint que exibe mensagem incrível
    """
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    request = Request()
    response = request.get_request_response(url)
    if restaurante is None:
        return {"Dados": response.json()}
    response_dict = request.get_json_field_as_list(response, "Company", restaurante, ["Item", "price", "description"])
    return {'Restaurante': restaurante, 'Cardapio': response_dict}