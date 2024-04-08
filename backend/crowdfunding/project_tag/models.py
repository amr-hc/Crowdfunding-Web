from django.db import models
from tags.models import Tag
from api.models import Project

class ProjectTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} - {self.project}'

    
    