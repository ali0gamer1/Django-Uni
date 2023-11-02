from django.urls import path
from .views import TermAPIView, TermListAPIView, UserAPIView, LoginAPIView, LogoutAPIView, ChangePasswordAPIView, \
    GetAllSubjectsAPIView, CreateSubjectAPIView, UpdateSubjectAPIView, DeleteSubjectAPIView, StudentsAPIView

urlpatterns = [
    path("term/<int:pk>/", TermAPIView.as_view()),
    path("terms/", TermListAPIView.as_view()),
    path("users/", UserAPIView.as_view()),
    path("users/login/", LoginAPIView.as_view()),
    path("users/logout/", LogoutAPIView.as_view()),
    path("users/changePassword", ChangePasswordAPIView.as_view()),
    path("subjects/get_all_subjects", GetAllSubjectsAPIView.as_view()),
    path("subjects/create_subject", CreateSubjectAPIView.as_view()),
    path("subjects/update/<int:pk>", UpdateSubjectAPIView.as_view()),
    path("subjects/delete/<int:pk>", DeleteSubjectAPIView.as_view()),
    path("students/"), StudentsAPIView.as_view()
]
