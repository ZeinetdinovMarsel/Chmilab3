from django.db import models
from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse

class Klasa(models.Model):
    titulli = models.CharField(max_length=150)
    pershkrimi = models.TextField(max_length= 200, null=True)
    imazhi = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')

    def __str__(self):
        return '{}'.format(self.titulli)

class Lendet(models.Model):
    krijues = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    titulli = models.CharField(max_length=30)
    klasa = models.ForeignKey(Klasa,on_delete=models.CASCADE)
    pershkrimi = models.TextField(max_length=400)
    krijuar_me = models.DateTimeField(auto_now=True)
    imazhi_lendes = models.ImageField(upload_to='kurs_images', default='default.jpg')

    def __str__(self):
        return self.titulli

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('pozicioni')


class LessonSchedule(models.Model):
    day_of_week = models.CharField(max_length=20)
    lesson_number = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    lenda = models.ForeignKey(Lendet,on_delete=models.CASCADE)
    teacher = models.CharField(max_length=50)
    cabinet = models.CharField(max_length=30)
    
    def __str__(self):
        return self.lenda
    
    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.lenda.slug,'lesson_slug':self.slug})


class Lesson(models.Model):
    slug = models.SlugField()
    titulli = models.CharField(max_length=30)
    lenda = models.ForeignKey(Lendet,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=11)
    pozicioni = models.IntegerField()

    def get_upload_path(instance, filename):
        return 'lesson_files/{}/{}'.format(instance.lenda.slug, filename)

    files = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return self.titulli

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.lenda.slug,'lesson_slug':self.slug})


