from django.contrib import admin
from django.urls import path

from users.apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('', admin.site.urls),
]
