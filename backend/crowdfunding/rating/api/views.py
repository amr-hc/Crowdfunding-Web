from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Rate
from rating.api.serializers import RatingSerializer

class RatingListCreateAPIView(ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RatingSerializer

class RatingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RatingSerializer
