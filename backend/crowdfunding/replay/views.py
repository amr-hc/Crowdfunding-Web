from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsOwnerOrReadOnly
from replay.models import Replay
from api.serializers import ReplaySerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
# Create your views here.
class ReplayModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer