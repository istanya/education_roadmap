from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
import json
# from app.edu.recommendations.recommend_questions import RecommendQuestions
module = Blueprint('edu', __name__, url_prefix ='/edu')


@module.route('/', methods=['GET'])
def education():
    mock_id = 5
    # quiz = RecommendQuestions().get_quiz(user_id=mock_id)
    quiz = [{'question': 'Как получить данные от пользователя?', 'correctAnswer': 2, 'answers':
    {1: 'Использовать метод get()', 2: 'Использовать метод input()', 3: 'Использовать метод readLine()', 4: 'Использовать метод read()'}}]
    return render_template('my_education.html', quiz=quiz)

@module.route('/', methods=['POST'])
def wrong_answers():
    ...
    return render_template('my_education.html', recommendations='')



