from django.shortcuts import render

from api.user.models import User
from .serializers import UserRegisterSerialzier, UserUpdateSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUser

class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerialzier
    
class UserEditApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsUser)
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return super().get_queryset()