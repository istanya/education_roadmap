import json
from app.edu.recommendations.recommend_questions import RecommendQuestions

class UserData:
    uinform = 'app/source/data/users_information.json'
    def __init__(self):
        self.read_info()
        self.skills = self.get_skills()
        self.tasks = self.get_tasks()
        self.recommended_courses = None
        self.recommended_questions = None
        self.model_recommendation = RecommendQuestions()

    def read_info(self):
        with open(self.uinform, 'r') as f:
            self.information = json.load(f)

    def get_skills(self):
        return self.information['skills']

    def get_tasks(self):
        return self.information['task']

    def get_recommended_courses(self):
        return recommended_courses

    def set_recommended_courses(self):
        self.recommended_courses = self.get_recommended_courses()

    def get_recommended_questions(self):
        recommended_questions = []
        indexes = []
        answers = []
        for s in self.skills:
            recommended_questions.extend(self.model_recommendation.filter(s, top_elem=5)[0])
            indexes.extend(self.model_recommendation.filter(s, top_elem=5)[1])
            answers.extend(self.model_recommendation.filter(s, top_elem=5)[2])
        return set(recommended_questions), set(indexes), set(answers)

    def set_recommended_questions(self):
        self.recommended_questions = self.get_recommended_questions()