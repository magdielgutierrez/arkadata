## REST API con Python, Flask y MySQL

Descripción:

Desarrollar un pipeline de análisis de datos utilizando los datos abiertos de la Ciudad de México correspondientes a las ubicaciones de las unidades del metrobús para que pueda ser consultado mediante un API REST filtrando por unidad o por alcaldía.

## Instrucciones

Primero, crear un entorno virtual:

  python -m virtualenv venv

Para instalar los paquetes necesarios:

  pip install -r requirements.txt

Crear un archivo .env (en la raíz del proyecto) para las variables de entorno:

    SECRET_KEY=SECRET_KEY
    
    MYSQL_HOST=host
    
    MYSQL_USER=user
    
    MYSQL_PASSWORD=password
   
    MYSQL_DATABASE=database

    MYSQL_PORT=database
    
 ## Dockerfile
 
 Crear contenedores
 
    docker-compose up -d
   
### Rutas:
Home  http://127.0.0.1:8000/api/

  1. .../list  | Obtener lista de registros 
  2. .../units | Obtener una lista de unidades disponibles  
  3. .../{vehicule_id} | Consultar la ubicación de una unidad dado su ID
  4. .../municipal | Obtener una lista de alcaldías disponibles
  5. .../{name_alcaldia} | Obtener la lista de unidades que se encuentren dentro de una alcaldía
 
 
 




