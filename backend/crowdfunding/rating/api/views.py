from rest_framework.viewsets import ModelViewSet
from api.models import Rate
from rating.api.serializers import RatingSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
class RatingAPIView(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Rate.objects.all()
    serializer_class = RatingSerializer

 
