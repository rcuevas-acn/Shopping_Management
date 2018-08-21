from flask import Blueprint, request
from app.modules.shopping_list.shopping_list_model import Items

items = Blueprint('items', __name__, url_prefix="/api")


@items.route("items", methods=['POST'])
def create():
    """Create items Model.

    Returns
    -------
        JSON: Shopping List Model
    """
    try:
        shopping_list_id = request.args.get('id')
        request_data = request.get_json()
        response = Items.create(request_data, shopping_list_id)
        return response, 200
    except Exception as error:
        print('Error {}'.format(error))
