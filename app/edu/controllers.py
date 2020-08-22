from flask import Blueprint
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify

module = Blueprint('edu', __name__, url_prefix ='/edu')


@module.route('/', methods=['GET'])
def education():
    return render_template('index.html')