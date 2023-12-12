# user_authentication/urls.py

from django.urls import path
from .views import UserLoginView, UserCreateView, UserLogoutView, GetAllUsersView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('get-all-users/', GetAllUsersView.as_view(), name='get_all_users'),
]
