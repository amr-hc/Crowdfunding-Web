from rest_framework.viewsets import ModelViewSet
from tags.models import Tag
from tags.api.serializers import TagSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
class TagAPIView(ModelViewSet):
    permission_classes = [AllowAny]

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

 
