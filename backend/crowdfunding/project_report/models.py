from django.db import models
from api.models import User
from api.models import Project

class Report(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    report=models.CharField( max_length=300,null=True, blank=True)

 
