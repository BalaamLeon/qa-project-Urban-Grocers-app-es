import data
import sender_stand_request


# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body


# Función para obtener el authToken de un usuario nuevo
def get_new_user_token():
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # Obtener el authToken de un nuevo usuario
    auth_token = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201

    # Comprueba que el campo name está en la respuesta y es igual al valor name del cuerpo de la solicitud
    assert kit_response.json()["name"] == name


# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_code_400(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # Obtener el authToken de un nuevo usuario
    auth_token = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400

    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. " \
                                             "De 2 a 15 caracteres"


# Función de prueba negativa cuando el error es "No se han aprobado todos los parámetros requeridos"
def negative_assert_no_name(kit_body):
    # Obtener el authToken de un nuevo usuario
    auth_token = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400

    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracter
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba 3. Error. El parámetro name contiene un string vacío
def test_create_kit_empty_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body("")
    # Comprueba la respuesta
    negative_assert_no_name(kit_body)


# Prueba 4. Error. El parámetro name contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Prueba 5. Kit creado con éxito. El parámetro name contiene caracteres especiales
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Prueba 6. Kit creado con éxito. El parámetro name contiene espacios
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("A Aaa")


# Prueba 7. Kit creado con éxito. El parámetro name contiene números
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# Prueba 8. Error. Falta el parámetro name en la solicitud
def test_create_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    kit_body = data.kit_body.copy()

    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")

    # Comprueba la respuesta
    negative_assert_no_name(kit_body)


# Prueba 9. Error. El tipo del parámetro name: número
def test_create_kit_number_type_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(12)

    # Obtener el authToken de un nuevo usuario
    auth_token = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprobar el código de estado de la respuesta
    assert kit_response.status_code == 400
