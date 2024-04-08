from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.models import User, Category , Project , Rate

from api.modelserializers import UserSerializer,LoginSerializer,CategorySerializer , ProjectSerializer,RateSerializer

from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet


from api.permissions import IsOwnerOrReadOnly, IsSameUserOrReadOnly,IsAdminOrReadOnly
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSameUserOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CategoryModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProjectModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer




class RateModelViewSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Rate.objects.all()
    serializer_class = RateSerializer