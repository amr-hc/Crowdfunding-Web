# SERIALIZERS MODULE
from rest_framework import serializers

# MODEL
from Donation.models import Donation
import datetime

# Donation Serializer
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

    def create(self, validated_data):
        if(validated_data['project'].end_date>datetime.date.today() or not validated_data['project'].hidden):
            raise serializers.ValidationError("Cant add donation")
        return super().create(validated_data)