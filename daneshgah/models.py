from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    degree = models.IntegerField()
    def __str__(self):
        return self.name + self.group

class AbstractCourse(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dependencies = models.ManyToManyField('AbstractCourse', blank=True, related_name="children")
    necessities = models.ManyToManyField('AbstractCourse', blank=True, related_name="sisters")
    credit = models.IntegerField()
    course_type = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class User(AbstractUser):
    uniquenum = models.CharField(max_length=20, default = "-1") ####### for creating a super user (temporary)
    phone_number = models.CharField(max_length=11, default="-1")
    national_id = models.CharField(max_length=10, default="-1")
    gender = models.BooleanField(default=False)
    birth_date = models.DateField(default="2000-01-01")
    pfp = models.FileField(
        storage = FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to = 'portraits',
        default = 'settings.MEDIA_ROOT/portraits/anon.png')
    def __str__(self):
        return self.username

class Professor(User):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    taught_courses = models.ManyToManyField(AbstractCourse, related_name="professorsdone")
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"
    def __str__(self):
        return self.username

class TermicCourse(AbstractCourse):
    course_time = models.TextField()
    exam_date = models.DateTimeField()
    exam_location = models.CharField(max_length=255)
    professor = models.ManyToManyField(Professor, related_name="termiccourses")
    capaciry = models.IntegerField()
    term = models.IntegerField()
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class IT(User):
    # implement an admin panel for this
    def __str__(self) -> str:
        return "IT"
    class Meta:
        verbose_name = "IT"
        verbose_name_plural = "ITs"

class DeputyofEducation(User):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Deputy of Education"
        verbose_name_plural = "Deputy of Educations"

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
