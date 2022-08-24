from items.items_model import Item
from main import db

class ItemsService:
    def __init__(self):
        self.Item = Item

    
    def get_all_items(self):
        items = self.Item.query.order_by(Item.price).all()
        return items

    def create_item(self, title, price):
        item = self.Item(title = title, price = price)
        try:
            db.session.add(item)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False