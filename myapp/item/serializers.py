from rest_framework import serializers
from .models import Product, Ingredient


class ProductSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredientsList', 'monthlySales')

    def get_imgUrl(self, product):
        imgUrl = f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/{product.imageId}.jpg'
        return imgUrl

class ProductDetailSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('imageId', 'ingredients')

    def imgUrl(self):
        return f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/{self.imageId}.jpg'


class ProductRecommendSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('imgUrl')

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price')

    def imgUrl(self):
        return f'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/{self.imageId}.jpg'
    

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
