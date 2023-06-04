from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from src.apps.users.api.views.students_groups import StudentGroupViewSet
from src.apps.users.api.views.users import UserViewSet, TeacherViewSet, StudentViewSet

# Импортировать все вьюсеты и создать роутер + зарегистрировать вьюсеты
# В ЮРЛпаттернс path("api/v1/", include(router.urls))

router = routers.DefaultRouter()
router.register("student-groups", StudentGroupViewSet)
router.register("users", UserViewSet)
router.register("teachers", TeacherViewSet)
router.register("students", StudentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(
#         "api/v1/users/",
#         include("src.apps.users.api.urls.users.router.urls")
#     ),
#     path(
#         "api/v1/students-groups/",
#         include("src.apps.users.api.urls.students_groups.router.urls")
#     ),
#     path("api/v1/", include("src.apps.api_auth.urls")),
#     path("api/v1/diary/", include("src.apps.student_diary.api.urls")),
# ]
