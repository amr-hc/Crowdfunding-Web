from rest_framework import serializers
from api.models import Rate
class RatingSerializer(serializers.ModelSerializer):

    def validate(self, data):
        data['user_id'] = self.context['request'].user
        return data
  
    class Meta:
        model = Rate
        fields = "__all__"  


