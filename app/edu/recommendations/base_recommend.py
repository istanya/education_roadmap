from abc import ABC, abstractmethod
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.edu.recommendations.embeddings import Elmo

class BaseRecommend(ABC):
    """ Базовый класс для рекомендаций """

    def __init__(self):
        self.model = Elmo()

    def get_cossimilarity(self, vector1, vector2):
        return 1 - cosine_similarity(vector1, vector2)

    def get_top_recommendations(self, label, variants, k=5):
        scores = []
        label = np.array(label).reshape(1, -1)

        for v in variants:
            v = np.array(v).reshape(1, -1)
            scores.append(self.get_cossimilarity(label, v)[0][0])
        top_k = np.array(scores).argsort()[-k:][::-1]
        return top_k


    @abstractmethod
    def get_(self, label):
        ...
