## REST API con Python, Flask y MySQL

Descripción:

Desarrollar un pipeline de análisis de datos utilizando los datos abiertos de la Ciudad de México correspondientes a las ubicaciones de las unidades del metrobús para que pueda ser consultado mediante un API REST filtrando por unidad o por alcaldía.

### Rutas:

1. obtener lista de registros
2. ddd
3. dd
4. 44
5. 55

## Instrucciones

Primero, crear un entorno virtual:

  python -m virtualenv venv

Para instalar los paquetes necesarios:

  pip install -r requirements.txt

Crear un archivo .env (en la raíz del proyecto) para las variables de entorno:

    SECRET_KEY=SECRET_KEY
    
    PGSQL_HOST=host
    
    PGSQL_USER=user
    
    PGSQL_PASSWORD=password
   
    PGSQL_DB=database
    
 ## Dockerfile
 
 Crear imagen para docker
 
    docker build -t restapi:v.1
   
 Crear contenerdor
 
  docker run --name localrestapi -p 6000:5000 -d restapi:v.1
 
 
 




