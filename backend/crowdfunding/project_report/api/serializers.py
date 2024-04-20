from rest_framework import serializers
from project_report.models import Report
class ReportSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    project_title = serializers.SerializerMethodField()
    class Meta:
        model = Report
        fields = "__all__"  

    def get_full_name(self,obj):
        return obj.user_id.first_name + " " +obj.user_id.last_name

    def get_project_title(self,obj):
        return obj.project_id.title
