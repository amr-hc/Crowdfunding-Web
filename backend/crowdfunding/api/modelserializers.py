from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from api.models import User, Category, Project, Rate, ImportantProject
from comment.models import Comment
from comment.serializer import CommentSerializer
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
        # fields = "__all__"
        fields = ["id", "email", "password", "first_name", "last_name", "is_superuser", "is_active", "birth_date", "photo","country","facebook","phone","owner_projects","donations"]
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
    donations = DonationSerializer(read_only=True, many=True)
    total_donations = serializers.SerializerMethodField()
    comments = CommentSerializer(read_only=True, many=True)
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

    def get_total_donations(self, obj):
        return sum(obj.donations.values_list('donation_amount', flat=True))


#
# class CommentSerializer(serializers.ModelSerializer):
#     user_data = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = "__all__"
#
#     def validate(self, data):
#         data['user_id'] = self.context['request'].user
#         return data
#
#     def get_user_data(self, obj):
#         user = obj.user_id
#         return {
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'image': user.photo.url if user.photo else None,  # Assuming photo is a FileField or ImageField
#             'country': user.country,
#             'is_active': user.is_active,
#             'is_superuser': user.is_superuser,
#         }

class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = "__all__"

class ReportCommentSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    comment=serializers.SerializerMethodField()
    project_id=serializers.SerializerMethodField()
    project_title=serializers.SerializerMethodField()
    class Meta:
        model = Report_comment
        fields = "__all__"

    def get_full_name(self,obj):
        return obj.user_id.first_name + " " +obj.user_id.last_name

    def get_comment(self,obj):
        return obj.comment_id.comment

    def get_project_id(self,obj):
        return obj.comment_id.project_id.id

    def get_project_title(self,obj):
        return obj.comment_id.project_id.title


class ImportantProjectSerializer(serializers.ModelSerializer):
    project=ProjectSerializer(read_only=True)
    project_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = ImportantProject
        fields = "__all__"

    def create(self, validated_data):
        if len(list(ImportantProject.objects.all())) >= 5:
            raise serializers.ValidationError("You Already Have 5 important projects")
        return super().create(validated_data)