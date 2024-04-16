from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from api.models import User, Category, Project, Rate, ImportantProject
from comment.models import Comment
from replay.models import Replay
from comment_report.models import Report_comment
from Project_Pics.api.serializer import ProjectPicsSerializer
from datetime import date

from Donation.api.serializer import DonationSerializer
from tags.api.serializers import TagSerializer
from tags.models import Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user']= request.user
        old = Rate.objects.filter(user=validated_data['user'],project=validated_data['project'])
        if old.exists():
            raise serializers.ValidationError("You Already Have rate for this project")
        return super().create(validated_data)


class ProjectWithoutOwner(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    pics = ProjectPicsSerializer(many=True, read_only=True)
    allrate = RateSerializer(many=True, read_only=True)
    average_rate = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
    def get_average_rate(self, obj):
        list_rates = list(obj.allrate.values_list('rate', flat=True))
        if len(list_rates)>0:
            avg = sum(list_rates) / len(list_rates)
        else:
            avg = 5
        return avg




class UserSerializer(serializers.ModelSerializer):
    owner_projects=ProjectWithoutOwner(read_only=True,many=True)
    donations=DonationSerializer(read_only=True,many=True)

    class Meta:
        model = User
        fields = "__all__"
        # fields = ["id", "email", "password", "first_name", "last_name", "is_superuser", "is_active", "birth_date", "photo","country","facebook","phone"]
        extra_kwargs = {'password': {'write_only': True}}
    def validate(self, data):
        if 'password' in data:
            data['password'] = make_password(data['password'])
        if data['birth_date'] >= date.today():
            raise serializers.ValidationError("You didn't born yet")
        return data



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class confirmActivation(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()



class userImportantData(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_superuser", "is_active", "birth_date", "photo","country","facebook","phone"]

class ProjectSerializer(serializers.ModelSerializer):
    owner = userImportantData(read_only=True)
    owner_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    pics = ProjectPicsSerializer(many=True, read_only=True)
    allrate = RateSerializer(many=True, read_only=True)
    average_rate = serializers.SerializerMethodField()
    tages= serializers.SlugRelatedField(many=True,slug_field='tagName',queryset=Tag.objects.all())

    class Meta:
        model = Project
        fields = "__all__"

    # def get_allrate(self, obj):
    #     list_rates = list(obj.allrate.values_list('rate', flat=True))
    #     if len(list_rates)>0:
    #         avg = sum(list_rates) / len(list_rates)
    #     else:
    #         avg = 5
    #     print(avg)
    #     return list(obj.allrate.values_list('rate', flat=True))

    def get_average_rate(self, obj):
        list_rates = list(obj.allrate.values_list('rate', flat=True))
        if len(list_rates)>0:
            avg = sum(list_rates) / len(list_rates)
        else:
            avg = 5
        return avg


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
    def validate(self, data):
        data['user_id'] = self.context['request'].user
        return data


class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = "__all__"

class ReportCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report_comment
        fields = "__all__"


class ImportantProjectSerializer(serializers.ModelSerializer):
    project=ProjectSerializer(read_only=True)
    project_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = ImportantProject
        fields = "__all__"