from config.config import ProductionConfig,DevelopmentConfig
from multiprocessing.sharedctypes import Value
from flask import Flask
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
app.config.from_object("config.config.ProductionConfig")

if __name__ == "__main__":
    app.run()