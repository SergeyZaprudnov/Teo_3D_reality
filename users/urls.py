from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UserConfig
from users.views import UserDetailView

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='user/user_login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
