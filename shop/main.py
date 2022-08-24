#from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

from items.src import items_registry
from app.src import base_registry


base_registry(app)

items_registry(app)

if __name__ == '__main__':
    app.run(debug=True)
