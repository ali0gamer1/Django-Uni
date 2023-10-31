from models import *

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProfessorSerializer(serializers.Serializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ITSerializer(serializers.Serializer):
    class Meta:
        model = IT
        fields = '__all__'

class DeputyofEducationSerializer(serializers.Serializer):
    class Meta:
        model = DeputyofEducation
        fields = '__all__'

class TermSerializer(serializers.Serializer):
    class Meta:
        model = Term
        fields = '__all__'

class RevisionRequestSerializer(serializers.Serializer):
    class Meta:
        model = RevisionRequest
        fields = '__all__'

class CourseStudentSerializer(serializers.Serializer):
    class Meta:
        model = CourseStudent
        fields = '__all__'

class EmergencyDropSerializer(serializers.Serializer):
    class Meta:
        model = EmergencyDrop
        fields = '__all__'

class TermDropSerializer(serializers.Serializer):
    class Meta:
        model = TermDrop
        fields = '__all__'

class EdCertSerializer(serializers.Serializer):
    class Meta:
        model = EdCert
        fields = '__all__'

class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Department
        fields = '__all__'

class FieldSerializer(serializers.Serializer):
    class Meta:
        model = Field
        fields = '__all__'

class SelectedCourseSerializer(serializers.Serializer):
    class Meta:
        model = SelectedCourse
        fields = '__all__'
