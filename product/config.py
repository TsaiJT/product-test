# built-in
import os, datetime, uuid
import urllib.parse


class Config(object):
    ALL_SERVICE_MODE = os.getenv("ALL_SERVICE_MODE")

    HOST = "127.0.0.1"
    PORT = 8899

    SECRET_KEY = uuid.uuid4().hex

    JSON_AS_ASCII = False

    # postgres db
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_CERT = os.getenv("POSTGRES_CERT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(POSTGRES_USER,
                                                                urllib.parse.quote_plus(POSTGRES_CERT),
                                                                POSTGRES_SERVER,
                                                                POSTGRES_PORT,
                                                                POSTGRES_DB)

class Production(Config):
    DEBUG = False


class Development(Config):
    DEBUG = True