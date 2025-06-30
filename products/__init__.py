from flask import Blueprint

# define blueprint for this app

product_bluprint = Blueprint('products', __name__, url_prefix='/products')

from app.products import views