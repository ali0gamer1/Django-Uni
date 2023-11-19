import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from daneshgah.models import TermicCourse
from daneshgah.serializers import TermicCourseSerializer

client = Client()


class GetAllSubjects(TestCase):
    def setUp(self):
        print('just getting started')

    def test_getAllCourseStudents(self):
        response = client.get(reverse('all_subjects'))
        subjects = TermicCourse.objects.all()
        serializer = TermicCourseSerializer(subjects, many=True)
        self.assertEqual(response.data, serializer.data) #authentication error!
