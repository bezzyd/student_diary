from django.contrib import admin
from src.apps.study.models.lessons import Lesson
from src.apps.study.models.subjects import Subject
from src.apps.study.models.tasks import Task
from src.apps.study.models.task_solutions import TaskSolution


admin.site.register(Lesson)
admin.site.register(Subject)
admin.site.register(Task)
admin.site.register(TaskSolution)
