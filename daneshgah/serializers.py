from .models import (User, Student, Professor, IT, DeputyofEducation, Term, RevisionRequest,
                     CourseStudent, EmergencyDrop, TermDrop, EdCert, Department, Field, SelectedCourse, TermicCourse,AbstractCourse)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ITSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT
        fields = '__all__'

class DeputyofEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeputyofEducation
        fields = '__all__'

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class RevisionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionRequest
        fields = '__all__'

class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudent
        fields = '__all__'

class EmergencyDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyDrop
        fields = '__all__'

class TermDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermDrop
        fields = '__all__'

class EdCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdCert
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class SelectedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedCourse
        fields = '__all__'

class TermicCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermicCourse
        fields = '__all__'

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'

class AbstractCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractCourse
        fields = '__all__'
