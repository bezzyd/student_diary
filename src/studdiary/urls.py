from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from src.apps.users.api.views.students_groups import StudentGroupViewSet
from src.apps.users.api.views.students import StudentViewSet
from src.apps.users.api.views.teachers import TeacherViewSet
from src.apps.users.api.views.users import UserViewSet

router = routers.DefaultRouter()
router.register("student-groups", StudentGroupViewSet)
router.register("users", UserViewSet)
router.register("teachers", TeacherViewSet)
router.register("students", StudentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls))]
