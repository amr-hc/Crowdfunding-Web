from django.urls import path
from project_report.api.views import ReportListCreateAPIView,ReportRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', ReportListCreateAPIView.as_view()),
    path('<int:id>/', ReportRetrieveUpdateDestroyAPIView.as_view()),
]



