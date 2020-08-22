from flask import Blueprint

module = Blueprint('edu', __name__, url_prefix ='/edu')


@module.route('/', methods=['GET'])
def index():
    return 'This Edu!'