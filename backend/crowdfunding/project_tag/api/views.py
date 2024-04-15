from rest_framework.viewsets import ModelViewSet
# from api.models import ProjectTag
# from project_tag.api.serializers import ProjectTagSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
# class ProjectTagAPIView(ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = ProjectTag.objects.all()
#     serializer_class = ProjectTagSerializer

 
