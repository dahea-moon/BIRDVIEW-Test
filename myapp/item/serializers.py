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
    recommends = serializers.SerializerMethodField('get_recommends')

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales', 'recommends')

    def get_imgUrl(self, product):
        imgUrl = f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/{product.imageId}.jpg'
        return imgUrl

    def get_recommends(self, product):
        skin_type = self.context['skin_type']
        queryset = Product.objects.exclude(id=product.id)
        queryset = queryset.order_by(f'-{skin_type}_score', 'price')[:3]
        return ProductRecommendSerializer(
            queryset,
            many=True,
        ).data


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
