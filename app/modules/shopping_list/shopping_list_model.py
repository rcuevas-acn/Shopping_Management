from flask import jsonify
from datetime import datetime
from app.services.sqlalchemy import db


class ShoppingList(db.Model):
    __tablename__ = "shoppinglist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    store_name = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @classmethod
    def create_table(cls):
        db.create_all()

    @classmethod
    def all(cls):
        items = []
        for i in db.session.query(cls).all():
            data = jsonify(
                id=i.id,
                title=i.title,
                store_name=i.store_name,
                date=i.date
            )
            items.append(data)
        return data


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'), nullable=False)
