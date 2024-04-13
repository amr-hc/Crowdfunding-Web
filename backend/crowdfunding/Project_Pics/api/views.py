
from rest_framework.viewsets import ModelViewSet

# Project Pics Model
from Project_Pics.models import ProjectPics

# Serializer
from Project_Pics.api.serializer import ProjectPicsSerializer

# Permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

class ProjectPicsViewSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = ProjectPics.objects.all()
    serializer_class = ProjectPicsSerializer
