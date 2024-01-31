
from django.views.generic import ListView

from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'