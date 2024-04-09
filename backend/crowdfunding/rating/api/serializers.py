from rest_framework import serializers
from api.models import Rate
class RatingSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Rate
        fields = "__all__"  


