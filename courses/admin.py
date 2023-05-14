from django.contrib import admin
from courses.models import Lendet,Lesson,Klasa,LessonSchedule
# Register your models here.

admin.site.register(Lendet)
admin.site.register(Lesson)
admin.site.register(Klasa)
admin.site.register(LessonSchedule)
