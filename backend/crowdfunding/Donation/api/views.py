"DRF (Django REST Framework) views for Crowdfunding.)"
# RESPONSE (Handled By : dabour1)
from rest_framework.response import Response

# ACTION (CUSTOM)
from rest_framework.decorators import action

# VIEWSETS
from rest_framework.viewsets import ModelViewSet

# PERMISSIONS
from rest_framework.permissions import AllowAny

from api.permissions import donation

"from Project"
# MODEL
from Donation.models import Donation

# SERIALIZER
from Donation.api.serializer import DonationSerializer


class DonationViewSet(ModelViewSet):
    permission_classes = [donation]
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    # Top Five Donations (Custom Action)
    @action(detail=False, methods=["get"])
    def top_five_donations(self, request):
        top_five = Donation.objects.order_by("-amount")[:5]
        serializer = self.get_serializer(top_five, many=True)
        return Response(serializer.data)
