from rest_framework import serializers

from api.models import User
# Comment Model
from .models import Comment
class CommentSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

    def validate(self, data):
        data['user_id'] = self.context['request'].user
        return data


    def get_user_data(self, obj):
        user = obj.user_id
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'image': user.photo.url if user.photo else None,  # Assuming photo is a FileField or ImageField
            'country': user.country,
            'is_active': user.is_active,
            'is_superuser': user.is_superuser,
            'rates': user.rates
        }
