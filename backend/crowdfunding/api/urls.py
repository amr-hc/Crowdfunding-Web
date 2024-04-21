from django.urls import path,include
from api.views import CategoryModelViewSet, ProjectModelViewSet, UserModelViewSet, login, RateModelViewSet, \
     ImportantProjectAPIView,confirmActivate
from comment.views import CommentModelViewSet
from comment_report.views import CommentReportModelViewSet
from replay.views import ReplayModelViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet)
router.register(r'users', UserModelViewSet)
router.register(r'categories', CategoryModelViewSet)
router.register(r'rate', RateModelViewSet),
router.register(r'ImportantProject', ImportantProjectAPIView),
router.register(r'comment', CommentModelViewSet),
router.register(r'replay', ReplayModelViewSet),

urlpatterns = [
    path('', include(router.urls)),
    path('login', login.as_view()),
    path('activate/', confirmActivate.as_view()),
]




