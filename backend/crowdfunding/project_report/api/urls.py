from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project_report.api.views import ReportAPIView

router = DefaultRouter()
router.register(r'', ReportAPIView)

urlpatterns = [
    path('', include(router.urls)),
]



