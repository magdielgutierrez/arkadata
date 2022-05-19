
import mysql.connector
from mysql.connector import Error
from decouple import config
from sqlalchemy import create_engine

    
def get_conexion_mysql():
       
    try:   
        return create_engine("mysql+pymysql://{user}:{pw}@{host}:{port}/{db}"
 				.format(host=config('MYSQL_HOST'),
                        db=config('MYSQL_DATABASE'),
                        port=config('MYSQL_PORT') ,
                        user=config('MYSQL_USER'),
                        pw=config('MYSQL_PASSWORD')))

    except Error as e:
            return e 
        