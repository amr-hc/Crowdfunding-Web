

from django.urls import path 
from project_tag.api.views import ProjectTagListCreateAPIView ,ProjectTagRetrieveUpdateDestroyAPIView
 

urlpatterns = [
    path('', ProjectTagListCreateAPIView.as_view()),
    path('<int:pk>/', ProjectTagRetrieveUpdateDestroyAPIView.as_view(), name='update&destroy'),
 
]




