from django.db import models

# Project Modle (Author Amr-hc)
from api.models import Project

class ProjectPics(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pics')
    image_path = models.ImageField(upload_to='images/project')

    # to String
    def __str__(self):
        return f"{self.project.name} - {self.id}"