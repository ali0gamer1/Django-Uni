from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField(max_length=20)

class Field(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    degree = models.IntegerField()
    
class AbstractCourse(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
    dependencies = models.ManyToManyField('AbstractCourse', blank=True)
    necessities = models.ManyToManyField('AbstractCourse', blank=True)
    credit = models.IntegerField()
    course_type = models.CharField(max_length=20)

class User(AbstractUser):
    uniquenum = models.CharField(max_length=20)
    #pfp = models.FileField(upload_to='/pfps')
    phone_number = models.CharField(max_length=11)
    national_id = models.CharField(max_length=10)
    gender = models.BooleanField(default=False)
    birth_date = models.DateField()

class Professor(User):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
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
    start_year = models.DateField()
    start_term = models.DateField()
    average_mark = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    passed_courses = models.ManyToManyField(TermicCourse)
    current_courses = models.ManyToManyField(TermicCourse)
    supervisor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    military_service = models.BooleanField(default=False)
    sanavat =models.IntegerField()

class IT(User):
    pass

class DeputyofEducation(User):
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
    field = models.ForeignKey(to=Field, on_delete=models.CASCADE)

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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(TermicCourse, on_delete=models.CASCADE)
    request = models.TextField()
    response = models.TextField()

class CourseStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(TermicCourse, on_delete=models.CASCADE)
    mark = models.FloatField(default=20.0)
    term = models.ManyToManyField(Term)

class EmergencyDrop(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(TermicCourse, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)
    request = models.TextField()
    response = models.TextField()

class TermDrop(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)
    request = models.TextField()
    response = models.TextField()

class EdCert(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)
    request = models.TextField()
    response = models.TextField()
    #file = models.FileField(upload_to='/edcerts')

class SelectedCourse(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(to=TermicCourse)
    admitted = models.BooleanField(default=False)
