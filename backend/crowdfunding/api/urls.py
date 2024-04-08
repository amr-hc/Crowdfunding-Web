

from django.urls import path,include
from api.views import testview,LoginAPIView,CategoryListCreateAPIView,ProjectModelViewSet,UserModelViewSet


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet)
router.register(r'users', UserModelViewSet)


urlpatterns = [
    path("categories", CategoryListCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('login/', include('django.contrib.auth.urls')),
    path('loginv/', LoginAPIView.as_view(), name='login'),

]




