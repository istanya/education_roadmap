import pandas as pd

class CheckAnswers:
    questions_filepath = 'app/source/data/Questions.csv'
    def __init__(self):
        self.read_question_file()

    def read_question_file(self):
        self.questions_df = pd.read_csv(self.questions_filepath)

    def check(self, answer_ind, id):
        return self.questions_df.loc[id]['correct_answer '] == answer_ind

