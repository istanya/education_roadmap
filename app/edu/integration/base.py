from abc import ABCMeta, abstractmethod
from collections import namedtuple


SourceRecomendation = namedtuple('SourceRecomendation', ['name', 'title', 'cover', 'link'])

class BaseIntegration(metaclass=ABCMeta):
    """Базовый класс для интеграции с обучающими ресурсами"""

    @abstractmethod
    def get_suorce_recomendations(self) -> [SourceRecomendation]:
        """
        Получает все источники для рекомендаций на заданном ресурсе
        """
        pass