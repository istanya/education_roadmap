from flask import Blueprint

module = Blueprint('chrome_extension', __name__, url_prefix ='/chrome_extension')


@module.route('/', methods=['GET'])
def index():
    return 'This Crome Extension!'