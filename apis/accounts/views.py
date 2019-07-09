from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from apis.accounts.models import User, Profile
from apis.accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

# class CreateUserApiView(APIView):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass

class CreateUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]