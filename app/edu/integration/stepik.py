from .base import BaseIntegration, SourceRecomendation
import requests
from collections import namedtuple

COUNT_POPULAR_COURSES = 4

Course = namedtuple('Course', ['id', 'name', 'cover'])


class StepikIntegration(BaseIntegration):
    """Класс обеспечивающий интеграцию с обучающим ресурсом Stepik"""

    URL_GET_COURSES_FILTER_PROF = 'https://stepik.org/api/search-results?' \
                                  'is_popular=true&is_public=true&page=1&query={prof}&type=course'
    URL_GET_COURSE = 'https://stepik.org/api/courses?ids[]={id_course}'
    URL_GET_SECTIONS = 'https://stepik.org/api/sections?{ids}'
    URL_GET_UNITS = 'https://stepik.org/api/units?{ids}'
    URL_GET_LESSONS = 'https://stepik.org/api/lessons?{ids}'
    URL_GET_EDU_LESSON = 'https://stepik.org/lesson/{id_lesson}/step/1'

    def get_suorce_recomendations(self):
        """
        Получает все источники для рекомендаций на ресурсе Stepik
        """

        source_recommendations = []
        response = requests.get(self.URL_GET_COURSES_FILTER_PROF.format(prof='python')).json()
        courses_resp = response['search-results']

        for course_resp in courses_resp[:COUNT_POPULAR_COURSES]:
            course_obj = Course(id=course_resp['target_id'],
                                name=course_resp['course_title'],
                                cover=course_resp['course_cover'])
            course_resp_new = requests.get(self.URL_GET_COURSE.format(id_course=course_obj.id)).json()
            sections = course_resp_new['courses'][0]['sections']
            section_ids = 'ids[]=' + '&ids[]='.join([str(el) for el in sections])
            sections_resp = requests.get(self.URL_GET_SECTIONS.format(ids=section_ids)).json()

            units = []
            for section_resp in sections_resp['sections']:
                units_patch = section_resp['units']
                units += units_patch

            unit_ids = 'ids[]=' + '&ids[]='.join([str(el) for el in units])
            units_resp = requests.get(self.URL_GET_UNITS.format(ids=unit_ids)).json()

            map_lessons_units = [unit_resp['lesson'] for unit_resp in units_resp['units']]
            lesson_ids = 'ids[]=' + '&ids[]='.join([str(el) for el in map_lessons_units])
            lessons_resp = requests.get(self.URL_GET_LESSONS.format(ids=lesson_ids)).json()
            for lesson_resp in lessons_resp['lessons']:
                lesson_link = self.URL_GET_EDU_LESSON.format(id_lesson=lesson_resp['id'])
                source_recommendation = SourceRecomendation(name=course_obj.name,
                                                            title=lesson_resp['title'],
                                                            cover=course_obj.cover,
                                                            link=lesson_link)
                source_recommendations.append(source_recommendation)

        return source_recommendations
