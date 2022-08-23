#from crypt import methods
from urllib import request
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import urllib.request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    isActive = db.Column(db.Boolean, default = True)
    def __repr__(self):
        return self.title

@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/buy/<int:id>')
def buy(id):
    return "Вы успешно купили "+str(id)

@app.get('/create')
def create_new_item_page():
   return render_template('create.html')

@app.post('/create')
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
