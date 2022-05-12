
import psycopg2 
from psycopg2 import DatabaseError, connection
from decouple import config

def get_connection_db():
    try: 
        return psycopg2.connect(
            host=config('MYSQL_HOST'),
            port=config('MYSQL_PORT'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            database=config('MYSQL_DATABASE')
         )
    except DatabaseError as ex:
        raise ex