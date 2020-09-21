from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_name=models.CharField(max_length=67)
    task_description=models.TextField()
    task_status=models.IntegerField(default=0)
    published_date=models.DateTimeField(default=datetime.now())
    due_date=models.DateTimeField()

    def __str__(self):
        return self.task_name;

class Information(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=67)
    reg_no=models.CharField(max_length=67)
    college_name=models.CharField(max_length=255)
    year=models.CharField(max_length=78)
    cgpa=models.FloatField(default=0.0)
