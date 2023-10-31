from django.db import models
from user.models import Professor, Student
from course.models import *
# Create your models here.
class Term(models.Model):
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(to=Student)
    professors = models.ManyToManyField(to=Professor)
    courses = models.ManyToManyField(to=TermicCourse)
    selection_start = models.DateTimeField()
    selection_end = models.DateTimeField()
    fix_start = models.DateTimeField()
    fix_end = models.DateTimeField()
    emergency_drop_end = models.DateTimeField()
    exam_start = models.DateTimeField()
    term_end = models.DateTimeField()
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
    file = models.FileField(upload_to='babali babooooo')#todo


class Department(models.Model):
    name = models.CharField(max_length=20)

# ino shayad bayad jabeja onim todo
class Field(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(to=Department)
    credits = models.IntegerField()
    degree = models.IntegerField()

class SelectedCourse(models.Model):
    student = models.ForeignKey(to=Student)
    courses = models.ManyToManyField(to=TermicCourse)
    admitted = models.BooleanField(default=False)




