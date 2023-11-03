from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.core.mail import send_mail  #TODO
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import TermSerializer, UserSerializer, TermicCourseSerializer, ProfessorSerializer, StudentSerializer
from rest_framework.generics import RetrieveAPIView

class TermListAPIView(generics.ListAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()


class TermAPIView(generics.RetrieveAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()
    lookup_field = "pk"  # pk is default


class UserAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        return Response(UserSerializer(queryset).data)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"status": "Logged in successfully"})
        else:
            return Response({"error": "Invalid username or password"}, status=400)


class LogoutAPIView(APIView):
    def post(self, request):
        request.auth.delete()
        logout(request)
        return Response({"log_out": "successfully logged out"})

class ChangePasswordAPIView(APIView):
    def post(self, request):
        password = request.data.get('password')
        newPassword = request.data.get('newPassword')
        username = request.data.get('username')
        password = request.data.get('password')
        # TODO: implement email verification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.password = newPassword
            return Response({"status": "ChangedPassword"})
        else:
            return Response({"error": "Unable to change password!"}, status=400)

class GetAllSubjectsAPIView(generics.ListAPIView):
    serializer_class = TermicCourseSerializer
    model = TermicCourse
    queryset = TermicCourse.objects.all()

class CreateSubjectAPIView(generics.CreateAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer
class UpdateSubjectAPIView(generics.UpdateAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer
class DeleteSubjectAPIView(generics.DestroyAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer

class GetSubjectAPIView(generics.RetrieveAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class GetAllProfessorsAPIView(generics.ListAPIView):
    serializer_class = ProfessorSerializer
    model = Professor
    queryset = Professor.objects.all()

class GetSpecificProfessorsAPIView(RetrieveAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()

class UpdateProfessorsAPIView(generics.UpdateAPIView):
    queryset = Professor.objects.all()


class GetAllStudentsAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

class GetSpecificStudentsAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class UpdateStudentsAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()

# Subjects
class CreateSubjectAPIView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ListSubjectsAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        faculty = self.request.query_params.get('faculty', None)
        name = self.request.query_params.get('name', None)
        queryset = Subject.objects.all()

        if faculty:
            queryset = queryset.filter(faculty=faculty)
        if name:
            queryset = queryset.filter(name=name)

        return queryset

class GetSubjectAPIView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class UpdateSubjectAPIView(generics.UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class DeleteSubjectAPIView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Courses
class CreateCourseAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ListCoursesAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        faculty = self.request.query_params.get('faculty', None)
        name = self.request.query_params.get('name', None)
        term = self.request.query_params.get('term', None)
        queryset = Course.objects.all()

        if faculty:
            queryset = queryset.filter(faculty=faculty)
        if name:
            queryset = queryset.filter(name=name)
        if term:
            queryset = queryset.filter(term=term)

        return queryset

class GetCourseAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UpdateCourseAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DeleteCourseAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Course
class UserCoursesByField(APIView):
    @login_required
    def get(self, request):
        user = request.user
        field_of_study = user.field_of_study
        related_courses = Course.objects.filter(subject__field_of_study=field_of_study)
        serialized_courses = [course.to_dict() for course in related_courses]
        return Response({"courses": serialized_courses})



