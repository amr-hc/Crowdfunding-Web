"""
URL configuration for crowdfunding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import include, path, re_path

urlpatterns = [
    path("api/", include("api.urls")),
    path("tags/", include("tags.api.urls")),
    path("rating/", include("rating.api.urls")),
    path("report/projects/", include("project_report.api.urls")),
    path("report/comment/", include("comment_report.urls")),
    path(
        "social_auth/",
        include(("social_auth.urls", "social_auth"), namespace="social_auth"),
    ),
    # Donation Path
    path("donation/", include("Donation.api.urls")),
    # Project Pics
    path("project/", include("Project_Pics.api.urls")),
    # Forget Password
    path("password/", include("Reset_Password.urls")),
    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
