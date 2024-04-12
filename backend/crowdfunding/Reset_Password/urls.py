
from django.urls import path
from .views import forget_password, reset_password

urlpatterns = [
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),
]
