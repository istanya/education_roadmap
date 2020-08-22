import pandas as pd
from app.edu.recommendations.base_recommend import BaseRecommend


class RecommendQuestions(BaseRecommend):
    """ Класс для рекомендаций вопросов для теста на основе знаний человека"""
    questions_filepath = 'app/source/data/Questions.csv'

    def __init__(self):
        super().__init__()
        self.read_question_file()

    def read_question_file(self):
        self.questions_df = pd.read_csv(self.questions_filepath)

    def get_questionswith_answers(self, ids_lst):
        filtered_df = self.questions_df.loc[ids_lst]
        index = filtered_df.index.tolist()
        question = filtered_df['question'].values.tolist()
        answers = filtered_df[['answer1', 'answer2','answer3', 'answer4']].values.tolist()
        return question, index, answers

    def all_questions(self):
        return self.questions_df.index.tolist(), self.questions_df['question'].values.tolist()

    def filter(self, skill):
        index, quest = self.all_questions()
        skill = self.model.get_vector(skill)
        questions_lst_emb = []
        for q in quest:
            questions_lst_emb.append(self.model.get_vector(q))
        top_indexes = self.get_top_recommendations(skill, quest, k=2)
        question, index, answers = self.get_questionswith_answers(top_indexes)
        return question, index, answers




