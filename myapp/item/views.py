from django.shortcuts import render, HttpResponse, Http404
from django.views.decorators.http import require_GET
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.schemas import AutoSchema
from .serializers import ProductSerializer, ProductDetailSerializer, ProductRecommendSerializer
from .models import Product, Ingredient, ProductScore
from .forms import ProductForm
# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class ProductDetail(generics.RetrieveAPIView):
#     def get()






@require_GET
def create_product(request):
    product_form = ProductForm(request.GET)
    if product_form.is_valid():
        product = product_form.save()
        ingredient_list = product.ingredientsList.split(',')
        oily_score, dry_score, sensitive_score = 0, 0, 0
        for ingredient in ingredient_list:
            target_ingredient = Ingredient.objects.get(name=ingredient)
            product.ingredients.add(target_ingredient)
            oily_score += target_ingredient.get_oily_score()
            dry_score += target_ingredient.get_dry_score()
            sensitive_score += target_ingredient.get_sensitive_score()
    
        ProductScore.objects.create(
            product=product,
            oily_score=oily_score,
            dry_score=dry_score,
            sensitive_score=sensitive_score
            )
        return HttpResponse('success')
    return Http404

        
