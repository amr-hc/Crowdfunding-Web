from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.models import User, Category , Project

from api.modelserializers import UserSerializer,LoginSerializer,CategorySerializer , ProjectSerializer

from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet



from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = authenticate(email=email, password=password)

        if user:
            return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

# class UserListCreateAPIView(ListCreateAPIView):
#     # permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CategoryListCreateAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def testview(request):
    return HttpResponse("hi")



