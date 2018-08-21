from flask import jsonify
from datetime import datetime
from app.services.sqlalchemy import db


class ShoppingList(db.Model):
    __tablename__ = "shoppinglist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    store_name = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    items = db.relationship('Items', backref='shoppinglist', lazy=True)

    @classmethod
    def create_table(cls):
        """Create all table in this model.
        """
        db.create_all()

    @classmethod
    def all(cls, parameter):
        """List Shopping List and Item Model.

        Parameters
        ----------
        parameter : JSON

        Returns
        -------
        JSON: Array List of Shopping List and Item Model
        """
        items = []
        queries = []
        if parameter['id'] is not None:
            queries.append(ShoppingList.id == parameter['id'])
        if parameter['title'] is not None:
            queries.append(ShoppingList.title.like("%"+parameter['title']+"%"))
        if parameter['item_id'] is not None:
            queries.append(Items.item_id == parameter['item_id'])
        if parameter['name'] is not None:
            queries.append(Items.name.like("%"+parameter['name']+"%"))
        for i in db.session.query(cls).outerjoin(Items).filter(*queries).all():
            data = ShoppingList.set_json_shopping_list(i)
            items.append(data)
        return jsonify(data=items)

    @classmethod
    def create(cls, request):
        """Create Shopping List Model.

        Parameters
        ----------
        request : JSON

        Returns
        -------
        JSON: Shopping List Model
        """
        data = ShoppingList.set_shopping_list(request)
        db.session.add(data)
        db.session.commit()
        return jsonify(ShoppingList.set_json_shopping_list(data))

    @classmethod
    def update(cls, request, shopping_list_id):
        """Update Shopping List Model.

        Parameters
        ----------
        request : JSON
        shopping_list_id : int

        Returns
        -------
            JSON: Shopping List Model
        """
        data = ShoppingList.query.get(shopping_list_id)
        for i in request:
            exec("data.{}='{}'".format(i,request[i]))
        db.session.commit()
        return jsonify(ShoppingList.set_json_shopping_list(data))

    @classmethod
    def delete(cls, shopping_list_id):
        """Delete Shopping List Model.

        Parameters
        ----------
        shopping_list_id : int

        Returns
        -------
            JSON: Shopping List Model
        """
        data = ShoppingList.query.get(shopping_list_id)
        db.session.delete(data)
        db.session.commit()
        return jsonify(ShoppingList.set_json_shopping_list(data))

    @classmethod
    def set_shopping_list(cls, data):
        """Set Shopping List Model.

        Parameters
        ----------
        data : JSON

        Returns
        -------
            MODEL: Shopping List Model
        """
        return ShoppingList(title=data['title'],
                            store_name=data['store_name'])

    @classmethod
    def set_json_shopping_list(cls, data):
        """Set Shopping List Model to JSON.

        Parameters
        ----------
        data : Shopping List Model

        Returns
        -------
            JSON: Shopping List and Items Model
        """
        result = {
            'id': data.id,
            'title': data.title,
            'store_name': data.store_name,
            'date': data.date,
            'items': Items.set_list_items(data.items)
        }
        return result


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'), nullable=False)

    @classmethod
    def create(cls, request, shopping_list_id):
        """Create items Model.

        Parameters
        ----------
        request : JSON
        shopping_list_id : int

        Returns
        -------
            JSON: Shopping List Model
        """
        for i in request['items']:
            item = Items.query.filter_by(shopping_list_id=shopping_list_id,item_id=i['item_id']).first()
            if item is None:
                data = Items.set_items(i, shopping_list_id)
                db.session.add(data)
                db.session.commit()
            else:
                item.quantity=item.quantity+i['quantity']
                db.session.commit()
        return jsonify(ShoppingList.set_json_shopping_list(ShoppingList.query.get(shopping_list_id)))

    @classmethod
    def set_items(cls, data, shopping_list_id):
        """Set Items Model.

        Parameters
        ----------
        data : JSON
        shopping_list_id : int

        Returns
        -------
            MODEL: Items Model
        """
        return Items(item_id=data['item_id'],
                     name=data['name'],
                     quantity=data['quantity'],
                     shopping_list_id=shopping_list_id)

    @classmethod
    def set_json_items(cls, data):
        """Set Items Model to JSON.

        Parameters
        ----------
        data : Items Model

        Returns
        -------
            JSON: Items Model
        """
        result = {
            'id': data.id,
            'item_id': data.item_id,
            'name': data.name,
            'quantity': data.quantity,
            'shopping_list_id': data.shopping_list_id
        }
        return result

    @classmethod
    def set_list_items(cls, data):
        """Set Items Model to ArrayList.

        Parameters
        ----------
        data : JSON

        Returns
        -------
            ArrayList: JSON of Items Model
        """
        result = []
        for i in data:
            result.append(Items.set_json_items(i))
        return result
