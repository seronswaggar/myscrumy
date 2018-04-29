from django.db import models

from django.utils import timezone



class ScrumyUser(models.Model):
    ScrumyUser_Role = (
        ('O', 'Owner'),
        ('A', 'Admin'),
        ('D', 'Developer'),
        ('QA', 'Quality Analyst')
    )

    Name= models.CharField(max_length=300)
    role=models.CharField(max_length=50, default='O', choices=ScrumyUser_Role)


    def __str__(self):
        return self.Name
        self.save()

class GoalStatus(models.Model):

    Goal_Status=(
        ('D','Done'),
        ('P','Pending'),
        ('V', 'Verified'),
    )

    ScrumyUser_Role = (
        ('O', 'Owner'),
        ('A', 'Admin'),
        ('D', 'Developer'),
        ('QA', 'Quality Analyst'),
    )
    Scrumy_Goals=(
	    ('W','Weekly Goals'),
        ('DA','Daily Task'),
    )
    status= models.CharField(max_length=50,  choices=Goal_Status)
    completed_on= models.DateTimeField(default=timezone.now)
    goals= models.CharField(max_length=100, default='DA', null= True, choices=Scrumy_Goals)
    verified_by = models.CharField(max_length=30, default='QA', choices=ScrumyUser_Role)
    verified_date = models.DateTimeField(default=timezone.now)


class ScrumyGoals(models.Model):

        def get_queryset(self):
            queryset = ScrumyGoals.objects.all()
            return queryset

        Scrumy_Goals = (
            ('W', 'Weekly Goals'),
            ('DA', 'Daily Task'),
        )


        ScrumyUser_Role=(
            ('O', 'Owner'),
            ('A', 'Admin'),
            ('D', 'Developer'),
            ('QA', 'Quality Analyst'),
        )

        scrumyuser_id = models.ForeignKey('ScrumyUser',  null=True, blank=True, on_delete=models.CASCADE)
        goalstatus= models.ForeignKey('GoalStatus', null=True,blank=True, default=400, on_delete=models.PROTECT)
        title=models.CharField(max_length=100, default='It\'s not easy')
        task = models.CharField(max_length=100, default='enter your task')
        task_id= models.IntegerField(default=400, null=False)
        moved_by=models.CharField(max_length=50, default='not moved')
        created_by=models.CharField(max_length=50, default='O',null=False)
        created_date=models.DateTimeField(default=timezone.now)
        time_of_status_change=models.DateTimeField(default=timezone.now, null=False)
        due_date=models.DateTimeField(blank=True, null=True)


        def get_absolute_url(self):
            return reverse('bayodescrumy:index')

        def publish(self):
            self.created_date=timezone.now()

        def __str__(self):
            return self.title
            self.save()

        def overdue_status(self):
            'Response based on date.'
            if self.due_date and datetime.date.today()>self.due_date:
                return True
            else:
                print('Failed Task')
