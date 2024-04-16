from rest_framework.viewsets import ModelViewSet
from api.models import Rate
from api.permissions import IsOwnerOrReadOnly
from rating.api.serializers import RatingSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
class RatingAPIView(ModelViewSet):
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    queryset = Rate.objects.all()
    serializer_class = RatingSerializer

 
