from django.db import models
from api.models import User
from comment.models import Comment

class Report_comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    report=models.CharField( max_length=300,null=True, blank=True)
