from django.urls import path

from .views import HomeView, TaskView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('task/<str:task_id>/', TaskView.as_view(), name='task'),
]