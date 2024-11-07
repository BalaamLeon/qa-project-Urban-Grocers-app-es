import configuration
import requests
import data


# Solicitud POST para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)


# Solicitud POST para crear un kit con token de usuario
def post_new_client_kit(kit_body, auth_token):
    kit_headers = data.headers.copy()
    kit_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, headers=kit_headers, json=kit_body)
