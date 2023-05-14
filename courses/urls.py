from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,delete_lesson,LessonScheduleView,AboutView,ContactView,CourseListView,edit_row, CourseDetailView,LessonDetailView, SearchView, krijo_klase,delete_row, krijo_lende, krijo_mesim

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('schedule/', LessonScheduleView.as_view(), name='schedule'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='kerko_kurs'),
    path('krijo/klase', krijo_klase, name='krijo_klase'),
    path('krijo/lende', krijo_lende, name='krijo_lende'),
    path('krijo/mesim', krijo_mesim, name='krijo_mesim'),
    path('delete/<int:row_id>/', delete_row, name='delete_row'),
    path('edit_row/<int:row_id>/', edit_row, name='edit_row'),
    path('delete_lesson/<str:rday_of_week>/<str:rlesson_number>/', delete_lesson, name='delete_lesson'),
]
