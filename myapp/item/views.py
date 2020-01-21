from django.shortcuts import render, HttpResponse, Http404
from django.views.decorators.http import require_GET

from rest_framework import generics, mixins, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import ProductSerializer, ProductDetailSerializer, ProductRecommendSerializer
from .models import Product, Ingredient
from .forms import ProductForm


class ProductList(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Product.objects.all()
        skin_type = self.request.query_params.get('skin_type', None)
        category = self.request.query_params.get('category', None)
        exclude_ingredient = self.request.query_params.get('exclude_ingredient', None)
        include_ingredient = self.request.query_params.get('include_ingredient', None)

        if category != None:
            queryset = queryset.filter(category=category)

        if include_ingredient != None:
            include_ingredient = include_ingredient.split(',')
            for ingredient in include_ingredient:
                target = Ingredient.objects.get(name=ingredient)
                queryset = queryset.filter(ingredients__in=[target])
        
        if exclude_ingredient != None:
            exclude_ingredient = exclude_ingredient.split(',')
            for ingredient in exclude_ingredient:
                target = Ingredient.objects.get(name=ingredient)
                has_exclude_ingredient = queryset.filter(ingredients__in=[target])
                queryset = queryset.difference(has_exclude_ingredient)

        if skin_type != None:
            queryset = queryset.order_by(f'-{skin_type}_score', 'price')

        return queryset

    def list(self, request):
        print(request.query_params)
        skin_type = self.request.query_params.get('skin_type', None)
        if skin_type == None:
            message = {'message': 'Error 400, skin type must be defined'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page != None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        return Response(response_list)


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    def get(self, request, *args, **kewargs):
        return self.retrieve(request, *args, **kwargs)






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

        product.oily_score = oily_score
        product.dry_score = dry_score
        product.sensitive_score = sensitive_score
        product.save()
        return HttpResponse('success')
    return Http404

        
