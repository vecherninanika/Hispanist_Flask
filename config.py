import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL")
    MAIL_PASSWORD = os.getenv("PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL")
    FLASK_ADMIN_SWATCH = "simplex"
