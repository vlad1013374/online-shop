#from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from items.src import items_registry
from src import base_registry

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)


base_registry(app)

items_registry(app)

if __name__ == '__main__':
    app.run(debug=True)
