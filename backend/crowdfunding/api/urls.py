from django.urls import path,include
from api.views import CategoryModelViewSet, ProjectModelViewSet, UserModelViewSet, login, RateModelViewSet, CommentListCreateAPIView , ReplayListCreateAPIView , ReportCommentListCreateAPIView


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet)
router.register(r'users', UserModelViewSet)
router.register(r'categories', CategoryModelViewSet)
router.register(r'rate', RateModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login', login.as_view()),
    path('comment',CommentListCreateAPIView.as_view()),
    path('replay',ReplayListCreateAPIView.as_view()),
    path('report_comment',ReportCommentListCreateAPIView.as_view()),
]




