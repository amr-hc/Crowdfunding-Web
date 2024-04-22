from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from api.modelserializers import CommentSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from api.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class CommentModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer