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
            data = ShoppingList.set_json_shopping_list(i)
            items.append(data)
        return jsonify(data=items)

    @classmethod
    def create(cls, data):
        data = ShoppingList.set_shopping_list(data)
        db.session.add(data)
        db.session.commit()
        return jsonify(ShoppingList.set_json_shopping_list(data))

    @classmethod
    def delete(cls, shopping_list_id):
        data = ShoppingList.query.get(shopping_list_id)
        db.session.delete(data)
        db.session.commit()
        return jsonify(id=shopping_list_id,
                       title=data.title)

    @classmethod
    def set_shopping_list(cls, data):
        return ShoppingList(title=data['title'],
                            store_name=data['store_name'])

    @classmethod
    def set_json_shopping_list(cls, data):
        result = {
            'id': data.id,
            'title': data.title,
            'store_name': data.store_name,
            'date': data.date
        }
        return result


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'), nullable=False)
