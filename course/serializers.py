from rest_framework import serializers
from .models import AbstractCourse, TermicCourse


class AbstractCourseSerializer(serializers.Serializer):
    class Meta:
        model = AbstractCourse
        fields = '__all__'


class TermicCourseSerializer(serializers.Serializer):
    class Meta:
        model = TermicCourse
        fields = '__all__'
