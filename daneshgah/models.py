
from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=20)
class Field(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(to=Department)
    credits = models.IntegerField()
    degree = models.IntegerField()

class AbstractCourse(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(to=Department)
    dependencies = models.ManyToManyField('AbstractUser', blank=True)
    necessities = models.ManyToManyField('AbstractCourse', blank=True)
    credit = models.IntegerField()
    course_type = models.CharField()
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
class Professor(User):
    department = models.ForeignKey(Department)
    field = models.ForeignKey(Field)
    expertise = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    taught_courses = models.ManyToManyField(AbstractCourse)
class TermicCourse(AbstractCourse):
    course_time = models.TextField()
    exam_date = models.DateTimeField()
    exam_location = models.CharField(max_length=255)
    professor = models.ManyToManyField(to=Professor)
    capaciry = models.IntegerField()
    term = models.IntegerField()

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





class IT(User):
    pass

class DeputyofEducation(User):
    department = models.ForeignKey(to=Department)
    field = models.ForeignKey(to=Field)






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




# ino shayad bayad jabeja onim todo


class SelectedCourse(models.Model):
    student = models.ForeignKey(to=Student)
    courses = models.ManyToManyField(to=TermicCourse)
    admitted = models.BooleanField(default=False)




