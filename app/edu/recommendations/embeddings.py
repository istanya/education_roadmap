import json
from allennlp.modules import Elmo
from allennlp.modules.elmo import batch_to_ids
from os.path import join
import numpy as np

class Elmo:
    """ Elmo класс модели, который считает векторные представления слов"""

    config_path = '/content/swb/checkpoint/options.json'
    weight_path = '/content/swb/checkpoint/weights.hdf5'

    def load_model(self):
        self.elmo_model = Elmo(self.config_path, self.weight_path, 1)

    def get_vector(self, word):
        idx = batch_to_ids([[word]])
        return self.elmo_model(idx)["elmo_representations"][0].squeeze().tolist()

    def get_sentence_vector(self, sentence):
        embeddings_vector = []
        for token in sentence:
            embeddings_vector +=  self.get_vector(token)
        return embeddings_vector

