from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile, DiaryRecord, Class, Subject, Lesson

admin.site.register(User)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(DiaryRecord)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Lesson)
