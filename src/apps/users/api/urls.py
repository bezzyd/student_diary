from django.urls import path, include
from rest_framework import routers

from src.apps.users.api.views import UserViewSet
from src.apps.users.api.views_students_group import AddStudentInGroup

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'student-groups/<str:studentgroup_pk>/add-student/',
        AddStudentInGroup.as_view(),
        name='add-student'
    ),
]
