from flask import render_template, redirect, request

def items_registry(app):
    from items.items_model import Item


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
    return app