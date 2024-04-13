# SERIALIZERS MODULE
from rest_framework import serializers

# MODEL
from Donation.models import Donation

# Donation Serializer
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
