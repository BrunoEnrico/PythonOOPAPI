import requests
from requests import Response

class Request:

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

    @staticmethod
    def get_json_field_as_list(response: Response, field: str, value: str, field_keys: list[str]) -> dict:
        response_list = []
        for item in response.json():
            if item[field] == value:
                response_list.append(
                    {key: item[key] for key in field_keys}
                )
        return response_list