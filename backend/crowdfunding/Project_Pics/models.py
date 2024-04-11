from django.db import models
from api.models import Project
class ProjectPics(models.Model):
    project_title = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='images/project')

    def __str__(self):
        return f"{self.project_title} - {self.id}"