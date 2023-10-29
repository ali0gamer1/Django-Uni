from django.db import models
from user.models import *
# Create your models here.

class AbstractCourse(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(to=Department)
    dependencies = models.ManyToManyField(to=AbstractCourse)#todo
    necessities = models.ManyToManyField(to=AbstractCourse)#todo
    credit = models.IntegerField()
    course_type = models.CharField()

class TermicCourse(AbstractCourse):
    course_time = models.TextField()
    exam_date = models.DateTimeField()
    exam_location = models.CharField(max_length=255)
    professor = models.ManyToManyField(to=Professor)
    capaciry = models.IntegerField()
    term = models.IntegerField()


