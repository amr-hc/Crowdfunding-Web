from rest_framework import serializers
from Donation.models import Donation
from api.models import Project



class DonationSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class ProjectSerializerEDIT(serializers.ModelSerializer):

    donations = DonationSerializerEDIT(read_only=True, many=True)
    total_donations = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"


    def get_total_donations(self, obj):
        return sum(obj.donations.values_list('donation_amount', flat=True))
