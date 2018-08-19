from flask import Flask
import constants
from app.modules.shopping_list.shopping_list_api import shopping_list
from app.services.sqlalchemy import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = constants.SQL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.register_blueprint(shopping_list)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(500)
def server_error(e):
    """Return a custom 500 error."""
    return 'Error while serving request', 500
