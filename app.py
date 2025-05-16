import requests
from requests import Response

class App:

    @staticmethod
    def get_request_response(url: str):
        return requests.get(url, verify=False)

    @staticmethod
    def convert_json_response_to_dict(response: Response, field_to_retrieve: str, keys: list[str]) -> dict:
        response_dict = {}
        for item in response.json():
            data_name = item[field_to_retrieve]
            if data_name not in response_dict:
                response_dict[data_name] = []

            response_dict[data_name].append(
                {key: item[key] for key in keys}
            )
        return response_dict
