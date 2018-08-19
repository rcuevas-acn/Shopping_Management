from flask import Blueprint, request, jsonify
from app.modules.shopping_list.shopping_list_model import ShoppingList

shopping_list = Blueprint('shopping_list', __name__, url_prefix="/api")


@shopping_list.before_request
def before_request():
    ShoppingList.create_table()


@shopping_list.route("shopping_list", methods=['GET'])
def get_all():
    try:
        return ShoppingList.all(), 200
    except Exception as error:
        print('Error {}'.format(error))


@shopping_list.route("shopping_list", methods=['POST'])
def create():
    try:
        request_data = request.get_json()
        print(request_data)
        response = ShoppingList.create(request_data)
        print(response)
        return response, 200
    except Exception as error:
        print('Error {}'.format(error))


@shopping_list.route("shopping_list", methods=['DELETE'])
def delete():
    try:
        shopping_list_id = request.args.get('id')
        print(shopping_list_id)
        return ShoppingList.delete(shopping_list_id), 200
    except Exception as error:
        print('Error {}'.format(error))