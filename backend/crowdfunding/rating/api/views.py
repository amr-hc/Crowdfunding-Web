from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rating.models import Rating
from rating.api.serializers import RatingSerializer

class RatingListCreateAPIView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
