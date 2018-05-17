import re
from transliterate import translit

from app import db

categories = db.Table('categories',
    db.Column('category_id', db.Integer, db.ForeignKey('product_category.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)


def stubify(_string):
    return translit(re.sub(' ', '_', _string.lower()), 'ru', reversed=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price_kopeck = db.Column(db.Integer)  # SQLite doesn't support Decimal, so using integer kopecks for demo purposes
    description = db.Column(db.Text())
    image_url = db.Column(db.String(255))
    categories = db.relationship('ProductCategory', secondary=categories, lazy='subquery',
                                 backref=db.backref('products', lazy=True))


class ProductCategory(db.Model):

    def __init__(self, name, stub=None):
        self.name = name
        self.stub = stub if stub else stubify(name)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    stub = db.Column(db.String(255))
