from flask import Blueprint
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
from app.edu.recommendations.userdata import UserData
module = Blueprint('edu', __name__, url_prefix ='/edu')


@module.route('/', methods=['GET'])
def education():
    # mock_user = UserData()
    # questions, indexes, answers = mock_user.get_recommended_questions()
    # print(questions)
    return render_template('elements.html', data={'questions':questions, 'indexes':indexes, 'answers':answers})