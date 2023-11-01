from django.urls import path
from .views import TermAPIView, TermListAPIView, UserAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path("term/<int:pk>/", TermAPIView.as_view()),
    path("terms/", TermListAPIView.as_view()),
    path("users/", UserAPIView.as_view()),
    path("users/login/", LoginAPIView.as_view()),
    path("users/logout/", LogoutAPIView.as_view())
]
