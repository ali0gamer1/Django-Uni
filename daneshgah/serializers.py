from models import *
class TermSerializer(serializers.Serializer):# noqa
    class Meta:
        model = Term
        fields = '__all__'
class RevisionRequestSerializer(serializers.Serializer):# noqa
    class Meta:
        model = RevisionRequest
        fields = '__all__'
class CourseStudentSerializer(serializers.Serializer):# noqa
    class Meta:
        model = CourseStudent
        fields = '__all__'
class EmergencyDropSerializer(serializers.Serializer):# noqa
    class Meta:
        model = EmergencyDrop
        fields = '__all__'
class TermDropSerializer(serializers.Serializer):# noqa
    class Meta:
        model = TermDrop
        fields = '__all__'
class EdCertSerializer(serializers.Serializer):# noqa
    class Meta:
        model = EdCert
        fields = '__all__'
class DepartmentSerializer(serializers.Serializer):# noqa
    class Meta:
        model = Department
        fields = '__all__'
class FieldSerializer(serializers.Serializer):# noqa
    class Meta:
        model = Field
        fields = '__all__'
class SelectedCourseSerializer(serializers.Serializer):# noqa
    class Meta:
        model = SelectedCourse
        fields = '__all__'