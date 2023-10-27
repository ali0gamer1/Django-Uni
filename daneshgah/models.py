from django.db import models
from user.models import *
from course.models import *
# Create your models here.
class RevisionRequest(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(TermicCourse)
    request = models.TextField() #this is where this begging may work :)))))
    response = models.TextField() #this is the response of the forgiving professor.

class CourseStudent(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(TermicCourse)
    mark = models.FloatField(default=20.0)
    term = models.ManyToManyField(Term)
class EmergencyDrop(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(TermicCourse)
    result = models.BooleanField(default=False)
    request = models.TextField()
    response = models.TextField()
class TermDrop(models.Model):
    student = models.ForeignKey(Student)
    term = models.ForeignKey(Term)
    result = models.BooleanField(default=False)
    request = models.TextField()
    response = models.TextField()
class EdCert(models.Model):
    student = models.ForeignKey(Student)
    result = models.BooleanField(default=False)
    request = models.TextField()
    response = models.TextField()



