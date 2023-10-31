from .models import *
class UserSerializer(serializers.Serializer):# noqa
    class Meta:
        model = User
        fields = '__all__'
class StudentSerializer(serializers.Serializer):# noqa
    class Meta:
        model = Student
        fields = '__all__'
class ProfessorSerializer(serializers.Serializer):# noqa
    class Meta:
        model = Professor
        fields = '__all__'
class ITSerializer(serializers.Serializer):# noqa
    class Meta:
        model = IT
        fields = '__all__'
class DeputyofEducationSerializer(serializers.Serializer):# noqa
    class Meta:
        model = DeputyofEducation
        fields = '__all__'