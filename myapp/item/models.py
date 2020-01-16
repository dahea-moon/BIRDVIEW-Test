from django.db import models

# Create your models here.
# 상품 클래스
class Products(models.Model):
    imageId = models.CharField(max_length=)
    name = models.CharField()
    price = models.IntegerField()
    gender = models.CharField(max_length=6)
    category = models.CharField()
    #ingredients =
    monthlySales = models.IntegerField()

# 성분 클래스
class Ingredients(models.Model):
    name = models.CharField()
    oily = models.CharField()
    dry = models.CharField()
    sensitive = models.CharField()


# 피부 타입별 상품의 성분 점수 클래스
class ProductScore(models.Model):
    product_id = models.ForeignKey()
    oily_score = models.IntegerField()
    dry_score = models.IntegerField()
    sensitive_score = models.IntegerField()





    