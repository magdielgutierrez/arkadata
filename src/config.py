from decimal import Clamped
from distutils.debug import DEBUG
from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    
class DevelopmentConfig(Config):
    DEBUG=True
    port= 6565

config={
    'development': DevelopmentConfig
}