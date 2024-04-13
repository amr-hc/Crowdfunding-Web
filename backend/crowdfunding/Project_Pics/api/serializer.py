from rest_framework.serializers import ModelSerializer

# Project Pics
from Project_Pics.models import ProjectPics

class ProjectPicsSerializer(ModelSerializer):
    class Meta:
        model = ProjectPics
        fields = '__all__'
