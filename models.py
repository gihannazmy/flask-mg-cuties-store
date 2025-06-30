from flask import url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key= True)
    price = db.Column(db.Integer)
    name = db.Column(db.String(200))
    description = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(50), nullable=True)

    def __str__(self):
        return f"{self.name}"
    @property
    def image_url(self):
        return url_for ('static', filename=f"products/{self.image}")

    @property
    def show_url(self):
        return url_for('students.show', product=self.id)
    @property
    def delete_url(self):
        return url_for('product.delete',product=self.id)

