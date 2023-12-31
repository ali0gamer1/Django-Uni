from django.urls import path
from .views import (
    TermAPIView,
    TermListAPIView,
    TermCoursesAPIView,
    UserAPIView,
    LoginAPIView,
    LogoutAPIView,
    ChangePasswordAPIView,
    GetAllSubjectsAPIView,
    CreateSubjectAPIView,
    UpdateSubjectAPIView,
    DeleteSubjectAPIView,
    RemainingTermAPIView,
    CourseSelectionAPIView,
    CourseSubstitutionAPIView,
    StudyingEvidencesAPIView,
    MyCoursesAPIView,
    PassCourseAPIView,
    CheckAllStudyingEvidenceAPIView,
    ProfessorApealRequestAPIView,
)

urlpatterns = [
    path("term/<int:pk>/", TermAPIView.as_view()),
    path("terms/", TermListAPIView.as_view()),
    path("users/", UserAPIView.as_view()),
    path("users/login/", LoginAPIView.as_view()),
    path("users/logout/", LogoutAPIView.as_view()),
    path("users/changePassword", ChangePasswordAPIView.as_view()),
    path("subjects/get_all_subjects", GetAllSubjectsAPIView.as_view(), name='all_subjects'),
    path("subjects/create_subject", CreateSubjectAPIView.as_view()),
    path("subjects/update/<int:pk>", UpdateSubjectAPIView.as_view()),
    path("subjects/delete/<int:pk>", DeleteSubjectAPIView.as_view()),
    path("student/<int:pk>/remaining-terms", RemainingTermAPIView.as_view()),
    path("student/<int:pk>/course-selection", CourseSelectionAPIView.as_view()),
    path("student/<int:pk>/course-substitution", CourseSubstitutionAPIView.as_view()),
    path("student/<int:pk>/studying-evidences", StudyingEvidencesAPIView.as_view()),
    path("student/<int:pk>/my-courses", MyCoursesAPIView.as_view()),
    path("student/<int:pk>/pass-course-report", PassCourseAPIView.as_view()),
    path("student/<int:pk>/term-courses", TermCoursesAPIView.as_view()),
    path(
        "assistant/<int:pk>/studying-evidence",
        CheckAllStudyingEvidenceAPIView.as_view(),
    ),
    path(
        "professor/<int:pk>/courses/<int:c_pk>/appeal-requests",
        ProfessorApealRequestAPIView.as_view(),
    ),
]
