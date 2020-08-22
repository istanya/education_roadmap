import pandas as pd
from app.edu.recommendations.base_recommend import BaseRecommend
from ..integration.stepik import StepikIntegration


class RecommendModules(BaseRecommend):
    """ Класс для рекомендаций обучающих ресурсов на основе тестирования"""

    def __init__(self):
        super().__init__()

    def get_fail_questions(self):
        return []

    def get_edu_sourse(self):
        return StepikIntegration().get_suorce_recomendations()

    def get_recom_cource(self, top_elem=2):
        recom_source = []
        sourses = self.get_edu_sourse()
        fail_questions = self.get_fail_questions()
        course_vect = [self.model.get_vector(sourse.title) for sourse in sourses]
        fail_question_vect = {fail_question: self.model.get_vector(fail_question) for fail_question in fail_questions}
        for question, question_vect in fail_question_vect.items():
            top_indexes = self.get_top_recommendations(question_vect, course_vect, k=top_elem)
            recom_source.append({question: course_vect[top_indexes]})
        return recom_source
