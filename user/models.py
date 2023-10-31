from django.db import models
from groups.models import *
from course.models import *
from daneshgah.models import *
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    uniquenum = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # pfp = image todo
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=11)
    national_id = models.CharField(max_length=10)
    gender =  models.CharField(max_length=255)# IS FEMALE CHERT BOOD
    birth_date = models.DateField
class Student(User):
    start_year = models.DateField()#IN HAM MITONE INT BASHE HAM DATE\
    start_term = models.DateField()
    average_mark = models.FloatField()
    department = models.ForeignKey(Department)
    field = models.ForeignKey(Field)
    passed_courses = models.ManyToManyField(TermicCourse) #todo
    current_courses = models.ManyToManyField(TermicCourse) #todo
    supervisor = models.ForeignKey(Professor)
    military_service = models.BooleanField(default=False)
    sanavat =models.IntegerField()

class Professor(User):
    department = models.ForeignKey(Department)
    field = models.ForeignKey(Field)
    expertise = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    taught_courses = models.ManyToManyField(AbstractCourse)



class IT(User):
    pass

class DeputyofEducation(User):
    department = models.ForeignKey(to=Department)
    field = models.ForeignKey(to=Field)
class DeputyofEducationSerializer(serializers.Serializer):# noqa
    class Meta:
        model = DeputyofEducation
        fields = '__all__'