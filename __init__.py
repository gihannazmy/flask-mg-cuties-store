from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import configuration_options
from app.models import db


def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = configuration_options[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"] = current_config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    # from app.products.views import index
    # app.add_url_rule('/products', view_func=index, endpoint='products.index')
    # i need to get the app to use bluprint

    from app.products import product_bluprint
    app.register_blueprint(product_bluprint)


    return app