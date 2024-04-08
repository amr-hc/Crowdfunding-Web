

from django.urls import path,include
from api.views import testview,UserListCreateAPIView,LoginAPIView,CategoryListCreateAPIView,ProjectModelViewSet


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet)

urlpatterns = [
    path("users", UserListCreateAPIView.as_view()),
    path("categories", CategoryListCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('login/', include('django.contrib.auth.urls')),
    path('loginv/', LoginAPIView.as_view(), name='login'),

]




