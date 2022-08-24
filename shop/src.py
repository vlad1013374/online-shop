from flask import render_template


def base_registry(app):
    from items.items_model import Item

    @app.route('/')
    def index():
        items = Item.query.order_by(Item.price).all()
        return render_template('index.html', items=items)

    @app.route('/about')
    def about():
        return render_template('about.html')

    return app