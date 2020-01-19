from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    # path(''),
    # path('<int:item_id>'),
    path('/create/', views.create_product, name='create_product')
]
