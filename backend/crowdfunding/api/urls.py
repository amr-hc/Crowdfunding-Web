from django.urls import path, include
from api.views import (CategoryModelViewSet,
                       ProjectModelViewSet,
                       UserModelViewSet,
                       login,
                       RateModelViewSet,
                       CommentListCreateAPIView,
                       ReplayListCreateAPIView,
                       ReportCommentListCreateAPIView,
                       send_test_email,

                       # Donation ViewSet
                       DonationViewSet,
                       # ProjectPics viewSet
                       ProjectPicsViewSet
                       )

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet)
router.register(r'users', UserModelViewSet)
router.register(r'categories', CategoryModelViewSet)
router.register(r'rate', RateModelViewSet)

# Donations Route
router.register(r'donations', DonationViewSet)
# ProjectPics Route
router.register(r'project_pics', ProjectPicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', login.as_view()),
    path('comment', CommentListCreateAPIView.as_view()),
    path('replay', ReplayListCreateAPIView.as_view()),
    path('report_comment', ReportCommentListCreateAPIView.as_view()),
    path('email/', send_test_email),
    # Top Five Donations (Custom Action)
    path('donations/top-five/', DonationViewSet.as_view({'get': 'top_five_donations'})),
]
