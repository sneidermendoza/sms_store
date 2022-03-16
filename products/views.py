from django.shortcuts import render

from django.views.generic.list import ListView

from products.models import Products
from django.views.generic.detail import DetailView

from .models import Products


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Products.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        print(context)
        return context

class ProductDetailview(DetailView):
    model = Products
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context