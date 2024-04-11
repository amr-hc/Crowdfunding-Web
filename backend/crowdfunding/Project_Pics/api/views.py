from rest_framework.viewsets import ModelViewSet

# Project Pics Model
from Project_Pics.models import ProjectPics

# Serializer
from Project_Pics.api.serializer import ProjectPicsSerializer

# Permissions
from rest_framework.permissions import AllowAny


class ProjectPicsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ProjectPics.objects.all()
    serializer_class = ProjectPicsSerializer
