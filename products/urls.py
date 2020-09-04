from django.urls import path
from . import views
from products.views import ProductDetailView, all_products

app_name = 'products'

urlpatterns = [

    path('', views.all_products, name='products'),

    path('<pk>/', ProductDetailView.as_view(), name='product_detail'),

]
