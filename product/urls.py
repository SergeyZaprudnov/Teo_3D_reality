from django import views
from django.urls import path

from product.apps import ProductConfig
from product.views import ProductListView, IndexView

app_name = ProductConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/', ProductListView.as_view(), name='product'),
]
