
import mysql.connector
from mysql.connector import Error
from decouple import config

def get_connection_db():
   
    try:
   
        mysql_config = {
                'user':config('MYSQL_USER'),
                'password':config('MYSQL_PASSWORD'),
                'host':config('MYSQL_HOST'),
                'database':config('MYSQL_DATABASE'),
                'port':config('MYSQL_PORT'),
                'ssl_disabled': True
            }
        
        cnxn_mysql = mysql.connector.connect(**mysql_config)
        return cnxn_mysql
        if cnx.is_connected():
            print("connected to database") 

    except Error as e:
            print("mysql DB connection error")
            print(e)
            
    
    

# try: 
       
#         psycopg2.connect(
#         #     # host=config('MYSQL_HOST'),
#         #     # port=config('MYSQL_PORT'),
#         #     # user=config('MYSQL_USER'),
#         #     # password=config('MYSQL_PASSWORD'),
#         #     # database=config('MYSQL_DATABASE')
#             dbname=database,
#             user=user,
#             password=passw,
#             host=host,
#             port=portdb,
            
#          )
        
    
#         print("holamund")
        
# except DatabaseError as ex:
#         print( "eroor de congggggggexon")
    
    
# import psycopg2
# from urllib.parse import urlparse

# conStr = "localhost://username:password@data_quality:5432"
# p = urlparse(conStr)

# pg_connection_dict = {
#     'dbname': database,
#     'user': user,
#     'password': passw,
#     'port': portdb,
#     'host': iphost,
#     'ssl_disabled': True

# }

# print(pg_connection_dict)
# con = psycopg2.connect(**pg_connection_dict)
# print(con)

