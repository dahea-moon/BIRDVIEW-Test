from django.shortcuts import render
from django.views.decorators.http import require_GET, require_GET
from .models import Product, Ingredient, ProductScore
from .forms import ProductForm
# Create your views here.

@require_GET
def create_product(request):
    ingredient_list = request.GET['ingredientsList']
    product_form = ProductForm(request.GET)
    if product_form.is_valid():
        product = product_form.save()
        for ingredient in ingredient_list:
            print(ingredient)
            q = Ingredient.objects.get(name=ingredient)
            product.ingredients.add(Ingredient.objects.get(name=ingredient))
        
        print('success')
    print('fail')
        
