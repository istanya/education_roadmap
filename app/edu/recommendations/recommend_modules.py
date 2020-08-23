import pandas as pd
from app.edu.recommendations.base_recommend import BaseRecommend
from ..integration.stepik import StepikIntegration
from app.edu.recommendations.embeddings import elmo_object

class RecommendModules(BaseRecommend):
    """ Класс для рекомендаций обучающих ресурсов на основе тестирования"""

    def __init__(self):
        super().__init__()

    def get_fail_questions(self):
        return []

    def get_edu_sourse(self):
        return StepikIntegration().get_suorce_recomendations()

    def get_recom_course(self, fail_questions, top_elem=5):
        recom_source = []
        sourses = self.get_edu_sourse()
        course_vect = [elmo_object.get_vector(sourse.title) for sourse in sourses]
        fail_question_vect = {fail_question: elmo_object.get_vector(fail_question) for fail_question in fail_questions}
        for question, question_vect in fail_question_vect.items():
            top_indexes = self.get_top_recommendations(question_vect, course_vect, k=top_elem)
            for index in top_indexes:
                recom_source.append(sourses[index])
        return recom_source


