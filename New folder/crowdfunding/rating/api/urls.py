

from django.urls import path 
from rating.api.views import RatingListCreateAPIView ,RatingRetrieveUpdateDestroyAPIView
 

urlpatterns = [
    path('', RatingListCreateAPIView.as_view()),
    path('<int:pk>/', RatingRetrieveUpdateDestroyAPIView.as_view(), name='update&destroy'),
 
]




