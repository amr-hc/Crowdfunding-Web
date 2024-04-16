from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Project_Pics.api.views import ProjectPicsViewSet

router = DefaultRouter()
router.register(r'photos', ProjectPicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
   ]