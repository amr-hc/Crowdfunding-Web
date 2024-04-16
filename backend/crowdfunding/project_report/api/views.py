from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAdminOrpost, IsOwnerOrAdmin
from project_report.models import Report
from project_report.api.serializers import ReportSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

class ReportListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminOrpost]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_url_kwarg = 'id'