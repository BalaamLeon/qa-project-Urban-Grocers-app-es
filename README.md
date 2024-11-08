# Proyecto Urban Grocers

> - Alumno: **Balaam Jesús Delgadillo León**
> - Grupo: **19**
> - Sprint: **7**

## Descripción

Conjunto de pruebas para comprobar el funcionamiento del endpoint **POST "/api/v1/kits"** de la aplicación **Urban Grocers**, 
centrándose en la validación del campo *name*.


## Documentación relevante de la API

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>/api/v1/kits</code></summary>

##### Información
Endpoint para crear una kit de una tarjeta específica o de usuario.

- Es obligatorio pasar el encabezado **Authorization** o el parámetro **cardId**, para crear la kit
- Si se recibe una solicitud con un encabezado **Authorization** que contenga el *authToken* de un/a usuario/a en particular - se creará la kit de este/a usuario/a.
- Si se recibe el parámetro **cardId**, se creará una kit dentro de la tarjeta correspondiente
- Si no se pasa ninguno de los parámetros, se devolverá un error.
- Cuando se pasan ambos parámetros, **Authorization** es la prioridad


##### Header

> | Campo          |  Tipo    | Tipo de dato | Descripción                                                                                                                           |
> |----------------|----------|--------------|---------------------------------------------------------------------------------------------------------------------------------------|
> | Authorization  | opcional | string       | Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las cestas creadas por el/la usuario/a. |
> | Content-Type   | opcional | string       | Valor por defecto: application/json                                                                                                   |


##### Ejemplo de encabezado

```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
```

##### Parámetro

> | Campo  | Tipo        | Tipo de dato | Descripción                                                                                                 |
> |--------|-------------|--------------|-------------------------------------------------------------------------------------------------------------|
> | cardId | opcional    | number       | El id de la tarjeta en la tabla card_model. Cuando se pasa - se creará un conjunto incluido en esta tarjeta |
> | name   | obligatorio | string       | El nombre de la kit, que será escrito en el campo correspondiente de la tabla kit_model.                    |


##### Ejemplos de respuesta

Respuesta: El conjunto ha sido creado con éxito
```http request
HTTP/1.1 201 Creado
```
```json
{
  "name": "Mi conjunto",
  "card": {
    "id": 1,
    "name": "Para la situación"
  },
  "productsList": null,
  "id": 7,
  "productsCount": 0
}
```

Error: No se ha transmitido ninguno de los parámetros
```http request
HTTP/1.1 400 Bad request.
```
```json
{
  "code": 400,
  "message": "No se han aprobado todos los parámetros requeridos"
}
```

Error: Validación del nombre
```http request
HTTP/1.1 400 Bad request.
```
```json
{
  "code": 400,
  "message": "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
}
```

Para más detalles sobre este endpoint, consulta la documentación de Crear un kit: [Main.Kits - Crear un kit](https://cnt-cf2f21c4-2ece-4efa-8ffb-816743e91675.containerhub.tripleten-services.com/docs/#api-Main.Kits-CreateKit)
</details>


## Requisitos

Para ejecutar estas pruebas, asegúrate de tener instalados Python y las librerías necesarias:

1. Instala [Python](https://www.python.org/downloads/) en tu sistema si aún no lo tienes.
2. Abre una terminal y ejecuta los siguientes comandos para instalar las librerías necesarias:
    ```shell
    pip install requests
    pip install pytest
    ```

## Ejecución de pruebas

Para ejecutar las pruebas de este proyecto:

1. Abre una terminal en la raíz del proyecto.
2. Usa el siguiente comando para ejecutar todas las pruebas:
    ```shell
    pytest create_kit_name_kit_test.py
    ```

3. Los resultados de las pruebas se mostrarán directamente en la terminal, indicando si cada prueba pasó o falló, junto con detalles adicionales en caso de errores.