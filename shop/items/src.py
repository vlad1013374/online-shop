from flask import render_template, redirect, request

def items_registry(app):
    from items.items_service import ItemsService
    items_service = ItemsService()

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
        if not items_service.create_item(title, price):
            return "Ошибка"     
        return redirect('/')
           
    return app