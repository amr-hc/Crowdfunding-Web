from api.models import Category, Project, Rate, User
from api.modelserializers import (
    CategorySerializer,
    CommentSerializer,
    LoginSerializer,
    ProjectSerializer,
    RateSerializer,
    ReplaySerializer,
    ReportCommentListCreateAPIView,
    UserSerializer,
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
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsSameUserOrReadOnly]
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReplayListCreateAPIView(ListCreateAPIView):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer


class ReportCommentListCreateAPIView(ListCreateAPIView):
    queryset = Report_comment.objects.all()
    serializer_class = ReportCommentListCreateAPIView


from django.core.mail import send_mail
from django.http import HttpResponse


def send_test_email(request):
    subject = "Test Email"
    message = "This is a test email sent from Django using Gmail SMTP."
    from_email = "amr.abdullah.elrefaey@gmail.com"  # Use your Gmail address here
    to_email = "ef64b54e13@emailbbox.pro"

    try:
        send_mail(subject, message, from_email, [to_email])
        return HttpResponse("Test email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send test email: {str(e)}")
