from rest_framework.viewsets import ModelViewSet
from project_report.models import Report
from project_report.api.serializers import ReportSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
class ReportAPIView(ModelViewSet):
    permission_classes = [AllowAny]
   
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

 
