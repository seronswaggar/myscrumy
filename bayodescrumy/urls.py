from django.urls import path
from . import views
from .models import ScrumyUser, ScrumyGoals, GoalStatus


urlpatterns = [
    path('', views.index, name='index'),

    path('<int:task_id>/', views.move_goal, name='move'),

    path('<scrumyuser_id>/', views.users, name='users'),



]
