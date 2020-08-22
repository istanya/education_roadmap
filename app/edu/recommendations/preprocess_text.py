# In case certificate verificatoin error
# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download('punkt')
# nltk.download('stopwords')

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
from string import punctuation, digits
import pymorphy2

stop_words = stopwords.words('russian')
pymorphy2m = pymorphy2.MorphAnalyzer()


class PreprocessText:
    """ Класс для предподготовки текста"""

    def __init__(self):
        self.cleaned_tokens = None
        self.cleaned_text = None

    def remove_spaces(self, text):
        text = text.strip()
        text = text.split()
        return ' '.join(text)

    def lower(self, text):
        return text.lower()

    def tokenize_t(self, text):
        return word_tokenize(text)

    def lemmatization(self, tokens):
        return [pymorphy2m.parse(x)[0].normal_form for x in tokens]

    def remove_punctuation(self, tokens):
        return [i for i in tokens if (i not in punctuation)]

    def remove_digits(self, tokens):
        return [i for i in tokens if (i not in digits)]

    def remove_stop_words(self, tokens):
        return [i for i in tokens if (i not in stop_words)]

    def get_cleaned_text_tokens(self):
        return self.cleaned_tokens

    def get_cleaned_text(self):
        return self.cleaned_text

    def clean(self, text):
        text = self.lower(text)
        text = self.remove_spaces(text)
        tokens = self.tokenize_t(text)
        lemmas = self.lemmatization(tokens)
        clean_tokens = self.remove_punctuation(lemmas)
        clean_tokens = self.remove_digits(clean_tokens)
        clean_tokens = self.remove_stop_words(clean_tokens)
        self.cleaned_tokens = clean_tokens
        self.cleaned_text = ' '.join(clean_tokens)
