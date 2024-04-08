from django.db import models
from api.models import User
from comment.models import Comment

class Replay(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    replay = models.CharField( max_length=500,null=True, blank=True)