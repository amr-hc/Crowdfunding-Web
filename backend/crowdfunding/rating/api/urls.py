from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating.api.views import RatingAPIView
 
router = DefaultRouter()
router.register(r'', RatingAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
