from flask import render_template
from items.items_service import ItemsService


def base_registry(app):
    items_service = ItemsService()

    @app.route('/')
    def index():
        items = items_service.get_all_items()
        return render_template('index.html', items=items)

    @app.route('/about')
    def about():
        return render_template('about.html')

    return app