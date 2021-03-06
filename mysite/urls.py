from django.contrib import admin
from django.urls import path

from core.views import  home, run_long_task, task_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('run-long-task/', run_long_task, name='run_long_task'),
    path('task-status/<str:task_id>/', task_status, name='task_status'),
]