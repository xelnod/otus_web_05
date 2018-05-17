from flask import Flask, request, render_template, abort
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import template_filters

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.register_blueprint(template_filters.blueprint)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Product, ProductCategory


@app.route('/', methods=['GET'])
def home():
    best_products = db.session.query(Product).limit(5).all()
    categories = db.session.query(ProductCategory).all()
    return render_template('index.html', categories=categories, best_products=best_products)


@app.route('/products/', methods=['GET'])
@app.route('/products/<string:category_stub>/', methods=['GET'])
def product_list(category_id=None, category_stub=None):
    categories = ProductCategory.query.all()
    if not category_id:
        category_id = request.args.get('category')
    if category_stub and not category_id:
        try:
            category_id = ProductCategory.query.filter_by(stub=category_stub).first().id
        except AttributeError:
            return abort(404)
    page = request.args.get('page') or 1
    query = db.session.query(Product)
    if category_id:
        query = query.filter(Product.categories.any(ProductCategory.id == category_id))
    try:
        queryset = query.paginate(page=int(page), per_page=10)
    except ValueError:
        return abort(404)
    return render_template('product_list.html', product_list=queryset, category_id=category_id, categories=categories)


@app.route('/products/<int:product_id>/', methods=['GET'])
def product_detail(product_id):
    product = db.session.query(Product).filter_by(id=product_id).first()
    if not product:
        return abort(404)
    return render_template('product_detail.html', product=product)
