from django.shortcuts import render
from django.views.generic import ListView

from product.models import Product


class IndexView(ListView):
    model = Product
    template_name = 'index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
