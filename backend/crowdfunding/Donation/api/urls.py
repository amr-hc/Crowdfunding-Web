from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Donation.api.views import DonationViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
