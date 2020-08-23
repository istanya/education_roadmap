from flask import Blueprint, render_template, request
from flask import request, redirect, url_for, jsonify
import json
import random
from app.edu.recommendations.recommend_questions import RecommendQuestions
from app.edu.recommendations.recommend_modules import RecommendModules
module = Blueprint('edu', __name__, url_prefix ='/edu')

cookies_users = set()


@module.route('/', methods=['GET'])
def education():
    mock_id = 5
    quiz = RecommendQuestions().get_quiz(user_id=mock_id)
    resp = render_template('my_education.html', quiz_questions=json.dumps(quiz), show=0)
    return resp

@module.route('/', methods=['POST'])
def wrong_question():
    wrong_q = json.loads(request.data.decode())['wrong_questions']
    modules = RecommendModules().get_recom_course(wrong_q)
    modules_hashmap = []
    for m in modules:
        elem = {}
        elem['name'] = m.name
        elem['title'] = m.title
        elem['cover'] = m.cover
        elem['link'] = m.link
        modules_hashmap.append(elem)
    return render_template('courses.html', recommendations=modules_hashmap, show=1)



