from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tags.api.views import TagAPIView
 
router = DefaultRouter()
router.register(r'', TagAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
 



