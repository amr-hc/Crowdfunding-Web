from django.db import models
from api.models import User
from api.models import Project

class Comment(models.Model):
    project_id = models.ForeignKey(Project, related_name="comments",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField( max_length=500,null=True, blank=True)


