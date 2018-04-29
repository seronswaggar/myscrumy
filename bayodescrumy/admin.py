from django.contrib import admin
from .models import ScrumyUser, ScrumyGoals, GoalStatus

admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoals)
admin.site.register(GoalStatus)
