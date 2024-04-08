from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tags.models import Tag
from tags.api.serializers import TagSerializer

class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
