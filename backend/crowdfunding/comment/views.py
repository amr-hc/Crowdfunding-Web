from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from api.modelserializers import CommentSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from api.permissions import IsOwnerCommentOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class CommentModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerCommentOrReadOnly]
    # permission_classes = [AllowAny]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer