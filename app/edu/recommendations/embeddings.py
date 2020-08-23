from deeppavlov.models.embedders.elmo_embedder import ELMoEmbedder


class Elmo:
    """ Elmo класс модели, который считает векторные представления слов"""

    model_url = 'app/source/models/elmo_ru-news_wmt11-16_1.5M_steps'

    def __init__(self):
        self.load_model()

    def load_model(self):
        self.elmo = ELMoEmbedder(self.model_url)

    def get_vector(self, word):
        return self.elmo([[word]]).tolist()[0]

    def get_sentence_vector(self, sentence):
        embeddings_vector = []
        for token in sentence:
            embeddings_vector += self.get_vector(token)
        return embeddings_vector

elmo_object = Elmo()