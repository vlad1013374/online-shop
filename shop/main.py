#from crypt import methods
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
from models.item_model import Item

@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items/buy/<int:id>')
def buy(id):
    return "Вы успешно купили "+str(id)

@app.get('/items/create')
def create_new_item_page():
   return render_template('create.html')

@app.post('/items/create')
def create_new_item():
    title = request.form['title']
    price = request.form['price']
    item = Item(title = title, price = price)
    try:
        db.session.add(item)
        db.session.commit()
        return redirect('/')
    except BaseException:
        return "Ошибка"

if __name__ == '__main__':
    app.run(debug=True)
