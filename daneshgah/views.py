from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail  # TODO
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Term,
    TermicCourse,
    AbstractCourse,
    Student,
    Professor,
    User,
    CourseStudent,
    EdCert, TermDrop, EmergencyDrop, RevisionRequest,
)
from .permissions import IsITPermission
from .serializers import (TermSerializer, UserSerializer, TermicCourseSerializer,
                          ProfessorSerializer, StudentSerializer,
                          AbstractCourseSerializer, TermDropSerializer, EmergencyDropSerializer,
                          CourseStudentSerializer, EdCertSerializer, RevisionRequestSerializer)
from rest_framework.generics import RetrieveAPIView


class TermListAPIView(generics.ListAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()


class TermAPIView(generics.RetrieveAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()
    lookup_field = "pk"
    permission_classes = [IsITPermission]


class UserAPIView(APIView):
    permission_classes = [IsITPermission]

    def get(self, request):
        queryset = User.objects.all()
        return Response(UserSerializer(queryset).data)


class LoginAPIView(APIView):
    permission_classes = [IsITPermission]

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
    permission_classes = [IsITPermission]

    def post(self, request):
        request.auth.delete()
        logout(request)
        return Response({"log_out": "successfully logged out"})


class ChangePasswordAPIView(APIView):
    permission_classes = [IsITPermission]

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
    permission_classes = [IsITPermission]
    serializer_class = TermicCourseSerializer
    model = TermicCourse
    queryset = TermicCourse.objects.all()


class CreateSubjectAPIView(generics.CreateAPIView):
    permission_classes = [IsITPermission]
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class UpdateSubjectAPIView(generics.UpdateAPIView):
    permission_classes = [IsITPermission]
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class DeleteSubjectAPIView(generics.DestroyAPIView):
    permission_classes = [IsITPermission]
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


class CreateSubjectAPIView(generics.CreateAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class ListSubjectsAPIView(generics.ListAPIView):
    serializer_class = TermicCourseSerializer

    def get_queryset(self):
        faculty = self.request.query_params.get('faculty', None)
        name = self.request.query_params.get('name', None)
        queryset = TermicCourse.objects.all()

        if faculty:
            queryset = queryset.filter(faculty=faculty)
        if name:
            queryset = queryset.filter(name=name)

        return queryset


class GetSubjectAPIView(generics.RetrieveAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class UpdateSubjectAPIView(generics.UpdateAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class DeleteSubjectAPIView(generics.DestroyAPIView):
    queryset = TermicCourse.objects.all()
    serializer_class = TermicCourseSerializer


class CreateCourseAPIView(generics.CreateAPIView):
    queryset = AbstractCourse.objects.all()
    serializer_class = AbstractCourseSerializer


class ListCoursesAPIView(generics.ListAPIView):
    serializer_class = AbstractCourseSerializer

    def get_queryset(self):
        faculty = self.request.query_params.get('faculty', None)
        name = self.request.query_params.get('name', None)
        term = self.request.query_params.get('term', None)
        queryset = AbstractCourse.objects.all()
        if faculty:
            queryset = queryset.filter(faculty=faculty)
        if name:
            queryset = queryset.filter(name=name)
        if term:
            queryset = queryset.filter(term=term)
        return queryset


class GetCourseAPIView(generics.RetrieveAPIView):
    queryset = AbstractCourse.objects.all()
    serializer_class = AbstractCourseSerializer


class UpdateCourseAPIView(generics.UpdateAPIView):
    queryset = AbstractCourse.objects.all()
    serializer_class = AbstractCourseSerializer


class DeleteCourseAPIView(generics.DestroyAPIView):
    queryset = AbstractCourse.objects.all()
    serializer_class = AbstractCourseSerializer


class UserCoursesByField(APIView):
    @login_required
    def get(self, request):
        user = request.user
        field_of_study = user.field_of_study
        related_courses = AbstractCourse.objects.filter(subject__field_of_study=field_of_study)
        serialized_courses = [course.to_dict() for course in related_courses]
        return Response({"courses": serialized_courses})


class RemainingTermAPIView(APIView):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            return Response({"sanavat": user.sanavat})
        else:
            return Response({'error': 'user not found'})


class CourseSelectionAPIView(APIView):
    def post(self, request, pk):
        courseID=request.POST.get('course')
        studentID= pk
        cs = CourseStudent.objects.create(courseID, studentID)
        cs.save()
        return Response({"the course student is created"})


class CourseSubstitutionAPIView(APIView):
    def post(self,request, pk):
        studentID = pk
        courseToBeRemovedID = request.POST.get('courseR')
        index = 1#todo number of CourseStudent we would like to delete#
        courseToBeRemoved=CourseStudent.objects.all()[index]
        courseToBeRemoved.delete()
        courseToBeAddedID = request.POST.get('CourseA')
        cs = CourseStudent.objects.create(courseToBeAddedID, studentID)
        cs.save()

class StudyingEvidencesAPIView(APIView):
    def get(self, request, pk):
        edCert = EdCert.objects.all().filter(student_id=pk)
        return Response({"edCert": edCert})

#RemoveTerm
class StudentTermRemovalRequestView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TermDropSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return TermDrop.objects.filter(student_id=student_id)


class AssistantTermRemovalRequestListView(generics.ListAPIView):
    serializer_class = TermDropSerializer
    queryset = TermDrop.objects.filter(status='pending')


class AssistantTermRemovalRequestDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = TermDropSerializer
    queryset = TermDrop.objects.all()
    lookup_url_kwarg = 's-pk'

#EmergencyRemove
class StudentEmergencyRemoveRequestView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmergencyDropSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        course_id = self.kwargs['course_id']
        return EmergencyDrop.objects.filter(student_id=student_id, course_id=course_id)


class AssistantEmergencyRemoveRequestListView(generics.ListAPIView):
    serializer_class = EmergencyDropSerializer
    queryset = EmergencyDrop.objects.filter(status='pending')


class AssistantEmergencyRemoveRequestDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = EmergencyDropSerializer
    queryset = EmergencyDrop.objects.all()
    lookup_url_kwarg = 's-pk'

class MyCoursesAPIView(APIView):
    def get(self, request, pk):
        currStudent = Student.objects.filter(student_id=pk)
        # currCourses = Student.objects.get(pk).current_courses.all()
        courseTakenBefore = Student.objects.get(pk).passed_courses.all()
        availableCourses = TermicCourse.objects.exclude(id__in=courseTakenBefore)
        serializer = TermicCourseSerializer(availableCourses, many=True)
        #todo show pishniaz and hamniaz foreach course, unable to test
        return Response(serializer.data)


class PassCourseAPIView(APIView):
    def get(self, request, pk):
        courseTakenBefore = Student.objects.get(pk).passed_courses.all()
        serializer = TermicCourseSerializer(courseTakenBefore, many=True)
        return Response(serializer.data)

class TermCoursesAPIView(APIView):
    def get(self, request, pk):
        courseTaken = Student.objects.get(pk).current_courses.all()
        serializer = TermicCourseSerializer(courseTaken, many=True)
        return Response(serializer.data)
class CheckAllStudyingEvidenceAPIView(generics.ListAPIView):
    serializer_class = EdCertSerializer
    queryset = EdCert.objects.all()
    # todo not sure about queryset

class ProfessorApealRequestAPIView(APIView):
    def get(self, pk, c_pk):
        appealRequests = RevisionRequest.objects.filter(course_id=c_pk)
        serializer = RevisionRequestSerializer(appealRequests, many=True)
        return Response(serializer.data)
