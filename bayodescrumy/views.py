from django.shortcuts import render

from django.http import HttpResponse
from .models import ScrumyUser

def index(request):
    return HttpResponse('Hello World!')


def users(request, scrumyuser_id):
    all_scrumyuser=ScrumyUser.objects.all()

    return HttpResponse('<br>'.join([u.Name for u in all_scrumyuser]))



def move_goal(request,task_id):
    return HttpResponse(task_id)