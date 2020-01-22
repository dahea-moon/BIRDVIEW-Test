from rest_framework import serializers
from .models import Product, Ingredient


class ProductSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales')

    def get_imgUrl(self, product):
        imgUrl = f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/{product.imageId}.jpg'
        return imgUrl


class ProductDetailSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')

    class Meta:
        model = Product
        exclude = ('imageId','ingredientsList', 'oily_score', 'dry_score', 'sensitive_score')

    def get_imgUrl(self, product):
        imgUrl = f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/{product.imageId}.jpg'
        return imgUrl


class ProductRecommendSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price')

    def get_imgUrl(self, product):
        imgUrl = f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/{product.imageId}.jpg'
        return imgUrl


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
