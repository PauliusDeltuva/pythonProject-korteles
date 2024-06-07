from datetime import datetime
from korteles import db


class card(db.Model):
    __tablename__ = 'cards'
    product_id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False, default='Kortele')
    price = db.Column(db.Float, nullable=False, default=10.0)
    created_date = db.Column(db.DateTime, default=datetime.now(), nullable=True)

    def __init__(self, product, price, ingredients, extra):
        self.product = product
        self.price = price
        self.ingredients = ingredients
        self.extra = extra

    def __repr__(self):
        return f'{self.product} - {self.price}'





