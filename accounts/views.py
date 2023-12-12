# user_authentication/views.py

from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data.get('email', '')
        password = data.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Login failed'}, status=401)

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data.get('email', '')
        password = data.get('password', '')

        if CustomUser.objects.filter(username=email).exists():
            return JsonResponse({'message': 'User with this email already exists'}, status=400)

        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        login(request, user)

        return JsonResponse({'message': 'User created and logged in'})


@method_decorator(csrf_exempt, name='dispatch')
class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({'message': 'Logout successful'})

class GetAllUsersView(View):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        user_list = [{'id': user.id, 'email': user.email} for user in users]
        return JsonResponse({'users': user_list})