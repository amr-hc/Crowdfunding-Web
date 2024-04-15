from django.urls import path

from social_auth.views import  FacebookSocialAuthView

urlpatterns = [
    path('facebook/', FacebookSocialAuthView.as_view()),

]