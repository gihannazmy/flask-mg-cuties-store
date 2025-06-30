from flask import render_template, request, url_for, redirect

from app.models import Product, db
from app.products import product_bluprint

@product_bluprint.route("", endpoint="index")
def index():
    products = Product.query.all()
    return render_template('products/index.html', products=products)

# @app.route('/products/<int:product>', endpoint='products.show')
@product_bluprint.route('<int:product>',endpoint='show')
def product_show(product):
    product = db.get_or_404(Product, product)
    return render_template('products/show_details.html', product=product)


# @app.route('/products/create', endpoint='products.create', methods=['GET', 'POSt'])
@product_bluprint.route('create', endpoint='create', methods=['GET', 'POSt'])
def product_create():
    if request.method == 'POST':
        product = Product(name=request.form["name"],price=request.form["price"],image=request.form["image"],description=request.form["description"])
        db.session.add(product)
        db.session.commit()
        return redirect(product.show_url)
    return render_template('products/create.html')


# @app.route('/products/delete/<int:product>', endpoint='product.delete')
@product_bluprint.route('delete', endpoint='delete')
def product_delete(product):

    product = db.get_or_404(Product, product)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.index'))