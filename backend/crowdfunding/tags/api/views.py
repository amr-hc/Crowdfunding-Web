from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from tags.models import Tag
from tags.api.serializers import TagSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
class TagAPIView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

 
