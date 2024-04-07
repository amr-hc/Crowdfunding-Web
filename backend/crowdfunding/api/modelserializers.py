from rest_framework import serializers

from api.models import User, Category , Project
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email", "password","first_name","last_name" ,"is_superuser","is_active", "birth_date","photo"]
        # fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Project
        fields = "__all__"