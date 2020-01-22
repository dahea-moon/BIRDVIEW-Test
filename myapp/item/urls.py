from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('products', views.ProductList.as_view(), name='product_list'),
    path('product/<int:product_id>', views.ProductDetail.as_view(), name='product_detail'),
    # path('create/', views.create_product, name='create_product')
]
