from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from project_tag.models import ProjectTag
from project_tag.api.serializers import ProjectTagSerializer

class ProjectTagListCreateAPIView(ListCreateAPIView):
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer

class ProjectTagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer
