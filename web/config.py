"""App configuration"""
from os import environ

# to be done somewhere:
# from dotenv import load_dotenv
# load_dotenv()
# or from command line
# source .env

class Config:
    """Set Flask configuration vars from .env file"""

    # General Config
    #SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    #SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    #SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    