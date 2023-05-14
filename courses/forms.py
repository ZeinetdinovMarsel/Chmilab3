from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson, LessonSchedule

class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titulli': 'Например, 11 класс или Класс информатики',
            'pershkrimi': 'Введите краткое описание класса',
            'imazhi': 'Можно загрузить фотографию класса или оставить поле пустым',
        }
        labels = {
            'titulli': 'Название класса',
            'pershkrimi': 'Описание',
            'imazhi': 'Загрузить фото',
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'titulli', 'klasa', 'pershkrimi', 'imazhi_lendes']
        help_texts = {
            'titulli': 'Например, Математика, География и т.д.',
            'pershkrimi': 'Введите краткое описание предмета',
            'klasa': 'Выберите класс, для которого создается предмет',
            'imazhi_lendes': 'Можно загрузить фотографию предмета или оставить поле пустым',
        }
        labels = {
            'titulli': 'Название предмета',
            'klasa': 'Класс',
            'pershkrimi': 'Описание',
            'imazhi_lendes': 'Загрузить фото',
        }
        
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['slug','titulli', 'lenda', 'video_id', 'pozicioni', 'files', ]
        help_texts = {
            'titulli':'Введите название урока',
            'lenda':'Выберите предмет, к которому относится данный урок',
            'video_id':'Введите идентификатор видео на YouTube, которое вы хотите загрузить (<a href="/media/youtube_help.png">где найти идентификатор</a>)',
            'pozicioni':'Укажите номер позиции или порядковый номер урока в рамках предмета',
            'files' : 'Файлы для обучения',
        }
        labels = {
            'titulli': 'Название урока',
            'lenda': 'Название предмета',
            'video_id': 'Видео id',
            'pozicioni': 'Номер урока',
            'files': 'Файл',



        }
        widgets = {
            'slug': forms.HiddenInput()
        }
            
class LessonScheduleForm(forms.ModelForm):
    class Meta:
        model = LessonSchedule
        fields = ['day_of_week', 'lesson_number','start_time','end_time', 'lenda', 'teacher', 'cabinet']
        help_texts = {
            'day_of_week':'Введите название урока',
            'lesson_number':'Выберите предмет, к которому относится данный урок',
            'start_time':'Введите время начала урока',
            'end_time':'Введите ремя конца урока',
            'lenda':'Выберите название предмета',
            'teacher':'Укажите номер позиции или порядковый номер урока в рамках предмета',
            'cabinet':'Укажите номер позиции или порядковый номер урока в рамках предмета',
        }
