from flask import Blueprint, jsonify
from app.modules.shopping_list.shopping_list_model import ShoppingList

shopping_list = Blueprint('shopping_list', __name__, url_prefix="/api")


@shopping_list.before_request
def before_request():
    ShoppingList.create_table()


@shopping_list.route("", methods=['GET'])
def get_all():
    return ShoppingList.all(), 200
