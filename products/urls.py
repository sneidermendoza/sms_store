from django.urls import path

from . import views

urlpatterns =[
    path('<pk>', views.ProductDetailview.as_view(), name='product')
]