# built-in
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv, find_dotenv

# 3rd
from flask import Flask

def create_app():
    app = Flask(__name__)

    load_dotenv(find_dotenv())
    app.config.from_object('config.Config')

    # select the service mode from config.py between class Production and class Development
    service_mode = {
        "development": "config.Development",
        "production": "config.Production"
    }.get(app.config['ALL_SERVICE_MODE'], "config.Production")

    app.config.from_object(service_mode)

    handler = RotatingFileHandler("runtime_log/runtime.log", maxBytes=10000000, backupCount=5)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s : %(message)s'))
    app.logger.addHandler(handler)


    return app

app = create_app()

