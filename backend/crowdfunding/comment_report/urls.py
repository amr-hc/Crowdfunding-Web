from django.urls import path

from rest_framework.routers import DefaultRouter

from comment_report.views import ReportListCreateAPIView, ReportRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ReportListCreateAPIView.as_view()),
    path('<int:id>/', ReportRetrieveUpdateDestroyAPIView.as_view()),
]
