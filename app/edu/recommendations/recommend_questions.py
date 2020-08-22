import pandas as pd

class RecommendQuestions:
    questions_filepath = ''

    def __init__(self):
        ...

    def read_question_file(self):
        questions_df = pd.read_csv(self.questions_filepath)



