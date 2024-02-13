from django.contrib import admin
from django.urls import path

from user.apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('', admin.site.urls),
]
