

from django.urls import path 
from tags.api.views import TagListCreateAPIView ,TagRetrieveUpdateDestroyAPIView
 

urlpatterns = [
    path('', TagListCreateAPIView.as_view()),
    path('<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='update&destroy'),
 
]




