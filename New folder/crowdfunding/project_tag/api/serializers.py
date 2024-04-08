from rest_framework import serializers
from project_tag.models import ProjectTag
class ProjectTagSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProjectTag
        fields = "__all__"  


