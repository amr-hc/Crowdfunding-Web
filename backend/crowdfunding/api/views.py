from djoser.compat import get_user_email,settings
from djoser import signals

from api.models import Category, Project, Rate, User, ImportantProject
from api.modelserializers import (
    CategorySerializer,
    CommentSerializer,
    LoginSerializer,
    ProjectSerializer,
    RateSerializer,
    ReplaySerializer,
    UserSerializer, ImportantProjectSerializer,
)
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsSameUserOrReadOnly
from comment.models import Comment
from comment_report.models import Report_comment
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from replay.models import Replay
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class login(ObtainAuthToken):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class UserModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSameUserOrReadOnly]
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save(*args, **kwargs)
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {"user": user}
        to = [get_user_email(user)]
        if settings.SEND_ACTIVATION_EMAIL:
            settings.EMAIL.activation(self.request, context).send(to)
        elif settings.SEND_CONFIRMATION_EMAIL:
            settings.EMAIL.confirmation(self.request, context).send(to)


class CategoryModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RateModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [AllowAny]
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class ImportantProjectAPIView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [AllowAny]
    queryset = ImportantProject.objects.all()
    serializer_class = ImportantProjectSerializer


