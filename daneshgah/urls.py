from django.urls import path
from .views import TermAPIView,TermListAPIView
urlpatterns = [
    path("term/<int:pk>/", TermAPIView.as_view()),
    path("terms/", TermListAPIView.as_view()),
    
]
