from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Term, User
from .serializers import TermSerializer, UserSerializer


class TermListAPIView(generics.ListAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()


class TermAPIView(generics.RetrieveAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()
    lookup_field = "pk"  # pk is default


class UserAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        return Response(UserSerializer(queryset).data)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"status": "Logged in successfully"})
        else:
            return Response({"error": "Invalid username or password"}, status=400)


class LogoutAPIView(APIView):
    def post(self, request):
        request.auth.delete()
        logout(request)
        return Response({"log_out": "successfully logged out"})

class ChangePasswordAPIView(APIView):
    def post(self, request):
        password = request.data.get('password')
        newPassword = request.data.get('newPassword')
        username = request.data.get('username')
        password = request.data.get('password')
        # TODO: implement email verification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.password = newPassword
            return Response({"status": "ChangedPassword"})
        else:
            return Response({"error": "Unable to change password!"}, status=400)
