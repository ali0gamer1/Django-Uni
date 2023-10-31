from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response_data = {'message': 'Login successful', 'username': username}
            # return JsonResponse(response_data)
            return Response(response_data)
        else:
            response_data = {'message': 'Login failed'}
            # return JsonResponse(response_data, status=401)
            return Response(response_data)
