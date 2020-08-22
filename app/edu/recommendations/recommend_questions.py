import pandas as pd
from app.edu.recommendations.base_recommend import BaseRecommend
from app.edu.recommendations.embeddings import elmo_object
from app.edu.recommendations.userdata import UserData

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
        correct_quesion = filtered_df['correct_answer '].values.tolist()
        return question, index, answers, correct_quesion

    def all_questions(self):
        return self.questions_df.index.tolist(), self.questions_df['question'].values.tolist()

    def filter(self, skill, top_elem=5):
        index, quest = self.all_questions()
        skill = elmo_object.get_vector(skill)
        questions_lst_emb = []
        for q in quest:
            questions_lst_emb.append(elmo_object.get_vector(q))
        top_indexes = self.get_top_recommendations(skill, questions_lst_emb, k=top_elem)
        question, index, answers, correct_quesion = self.get_questionswith_answers(top_indexes)
        return question, index, answers, correct_quesion


    def create_test_format(self, recommended_questions, indexes, answers, correct):
        quiz = []
        uniq_questions = set()
        for i, j, k in zip(recommended_questions, answers, correct):
            if i not in uniq_questions:
                quiz_elem = {}
                quiz_elem['question'] = i
                quiz_elem['correctAnswer'] = k
                quiz_elem['answers'] = {}
                for ind, ans in enumerate(j):
                    quiz_elem['answers'][ind + 1] = ans
                quiz.append(quiz_elem)
                uniq_questions.add(i)
        return quiz

    def get_quiz(self, user_id):
        recommended_questions, indexes, answers, correct = self.get_recommended_questions(user_id)
        return self.create_test_format(recommended_questions, indexes, answers, correct)

    def get_recommended_questions(self, user_id):
        skills = UserData().get_skills(id=user_id)
        recommended_questions = []
        indexes = []
        answers = []
        correct = []
        for s in skills:
            rec_filter = self.filter(s, top_elem=5)
            recommended_questions.extend(rec_filter[0])
            indexes.extend(rec_filter[1])
            answers.extend(rec_filter[2])
            correct.extend(rec_filter[3])
        return recommended_questions, indexes, answers, correct




