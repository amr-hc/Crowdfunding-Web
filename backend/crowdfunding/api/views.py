from django_filters.rest_framework import DjangoFilterBackend
from api.Filter import ProjectModelFilter
from api.models import Category, Project, Rate, User, ImportantProject
from api.serializers import (
    CategorySerializer,
    ProjectSerializer,
    RateSerializer,
    UserSerializer,
    ImportantProjectSerializer,
    confirmActivation,
)
from api.permissions import (
    IsAdminOrReadOnly,
    IsOwnerProjectOrReadOnly,
    IsSameUserOrReadOnly,
)

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet
from Project_Pics.models import ProjectPics
from api.pagination import small
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "is_superuser": user.is_superuser,
                "userName": user.first_name + " " + user.last_name,
            }
        )
    def delete(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserModelViewSet(ModelViewSet):
    permission_classes = [IsSameUserOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["email"]

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save(*args, **kwargs)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        subject = "Confirm account Crowdfunding"
        reset_link = f"http://localhost:8080/congs?uid={uid}&token={token}"
        message = f'welcome to Crowdfunding, to confirm your new account please click on <a href="{reset_link}">Click here</a>'
        from_email = "amr.abdullah.elrefaey@gmail.com"
        to_email = user.email
        send_mail(subject, message, from_email, [to_email])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_superuser and request.user != instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        user = authenticate(
            username=request.user.email, password=request.data["password"]
        )
        if user is not None:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerProjectOrReadOnly]
    pagination_class = small
    queryset = Project.objects.all().filter(hidden=False).order_by('-id')
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectModelFilter

    def perform_create(self, serializer):
        project = serializer.save()
        allPhotos = self.request.FILES.getlist("photos")
        for photo in allPhotos:
            newPhoto = ProjectPics()
            newPhoto.image_path = photo
            newPhoto.project = project
            newPhoto.save()


    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.queryset = Project.objects.all()
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.queryset = Project.objects.all()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RateModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class ImportantProjectAPIView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ImportantProject.objects.all()
    serializer_class = ImportantProjectSerializer


class confirmActivate(APIView):

    def post(self, request):
        serializer = confirmActivation(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data.get("uid")
            token = serializer.validated_data.get("token")
            try:
                uid = str(urlsafe_base64_decode(uid), "utf-8")
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if (
                user
                and not user.is_active
                and default_token_generator.check_token(user, token)
            ):
                user.is_active = True
                user.save()
                return Response(
                    {"message": "Account activated successfully."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Invalid activation link."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

