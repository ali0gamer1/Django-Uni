from django.contrib import admin
from .models import (
    User,
    Student,
    Professor,
    IT,
    DeputyofEducation,
    Term,
    RevisionRequest,
    CourseStudent,
    EmergencyDrop,
    TermDrop,
    EdCert,
    Department,
    Field,
    SelectedCourse,
    AbstractCourse,
    TermicCourse,
)

admin.site.register(Department)
admin.site.register(Field)
admin.site.register(AbstractCourse)
admin.site.register(User)
admin.site.register(Professor)
admin.site.register(TermicCourse)
admin.site.register(Student)
admin.site.register(IT)
admin.site.register(DeputyofEducation)
admin.site.register(Term)
admin.site.register(RevisionRequest)
admin.site.register(CourseStudent)
admin.site.register(EmergencyDrop)
admin.site.register(TermDrop)
admin.site.register(EdCert)
admin.site.register(SelectedCourse)
