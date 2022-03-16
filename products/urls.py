from django.urls import path

from . import views

urlpatterns =[
    path('<slug:slug>', views.ProductDetailview.as_view(), name='product')
]