from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=20)

class Field(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    degree = models.IntegerField()
    
class AbstractCourse(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dependencies = models.ManyToManyField('AbstractCourse', blank=True, related_name="parents")
    necessities = models.ManyToManyField('AbstractCourse', blank=True, related_name="sisters")
    credit = models.IntegerField()
    course_type = models.CharField(max_length=20)

class User(AbstractUser):
    uniquenum = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    national_id = models.CharField(max_length=10)
    gender = models.BooleanField(default=False)
    birth_date = models.DateField()
    pfp = models.FileField(
        storage = FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to = 'portraits',
        default = 'settings.MEDIA_ROOT/portraits/anon.png')

class Professor(User):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    taught_courses = models.ManyToManyField(AbstractCourse, related_name="professorsdone")

class TermicCourse(AbstractCourse):
    course_time = models.TextField()
    exam_date = models.DateTimeField()
    exam_location = models.CharField(max_length=255)
    professor = models.ManyToManyField(Professor, related_name="termiccourses")
    capaciry = models.IntegerField()
    term = models.IntegerField()

class Student(User):
    start_year = models.DateField()
    start_term = models.DateField()
    average_mark = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    passed_courses = models.ManyToManyField(TermicCourse, related_name="studentswhopassed")
    current_courses = models.ManyToManyField(TermicCourse, related_name="studentsstudying")
    supervisor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    military_service = models.BooleanField(default=False)
    sanavat =models.IntegerField()

class IT(User):
    # implement an admin panel for this
    pass

class DeputyofEducation(User):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

class Term(models.Model):
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(Student, related_name="terms")
    professors = models.ManyToManyField(Professor, related_name="asatid")
    courses = models.ManyToManyField(TermicCourse, related_name="courses")
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
    term = models.ManyToManyField(Term, related_name="FixME")

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
    file = models.FileField(
        storage = FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to = 'educerts',
        default = 'settings.MEDIA_ROOT/educerts/nothing.pdf')

class SelectedCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(TermicCourse, related_name="courses2")
    admitted = models.BooleanField(default=False)
