from rest_framework import serializers
from Donation.api.projectSerializerEdit import ProjectSerializerEDIT
from Donation.models import Donation
import datetime



# Donation Serializer
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

    def create(self, validated_data):
        project = validated_data['project']
        project_serializer = ProjectSerializerEDIT(project)

        if(project.end_date<datetime.date.today() or project.hidden or validated_data['project'].target_money < validated_data['donation_amount']+project_serializer.data["total_donations"]):
            raise serializers.ValidationError("Cant add donation")
        return super().create(validated_data)