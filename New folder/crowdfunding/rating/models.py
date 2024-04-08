from django.db import models
from api.models import User
from api.models import Project

class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    rate=models.IntegerField( null=True, blank=True)

    
