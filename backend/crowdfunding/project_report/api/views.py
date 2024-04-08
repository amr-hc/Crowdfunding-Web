from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from project_report.models import Report
from project_report.api.serializers import ReportSerializer

class ReportListCreateAPIView(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
