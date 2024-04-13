from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from api.modelserializers import CommentSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
# Create your views here.
class CommentModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer