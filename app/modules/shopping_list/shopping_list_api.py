from flask import Blueprint, request
from app.modules.shopping_list.shopping_list_model import ShoppingList

shopping_list = Blueprint('shopping_list', __name__, url_prefix="/api")


@shopping_list.before_request
def before_request():
    ShoppingList.create_table()


@shopping_list.route("shopping_list", methods=['GET'])
def get_all():
    try:
        parameter = {
            "id": request.args.get('id'),
            "title": request.args.get('title'),
            "item_id": request.args.get('item_id'),
            "name": request.args.get('name')
        }
        return ShoppingList.all(parameter), 200
    except Exception as error:
        print('Error {}'.format(error))


@shopping_list.route("shopping_list", methods=['POST'])
def create_update():
    try:
        shopping_list_id = request.args.get('id')
        request_data = request.get_json()
        if shopping_list_id is None:
            response = ShoppingList.create(request_data)
        else:
            response = ShoppingList.update(request_data, shopping_list_id)
        return response, 200
    except Exception as error:
        print('Error {}'.format(error))


@shopping_list.route("shopping_list", methods=['DELETE'])
def delete():
    try:
        shopping_list_id = request.args.get('id')
        return ShoppingList.delete(shopping_list_id), 200
    except Exception as error:
        print('Error {}'.format(error))
