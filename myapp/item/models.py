from django.db import models

# 성분 클래스
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    oily = models.CharField(max_length=1, blank=True)
    dry = models.CharField(max_length=1, blank=True)
    sensitive = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.name

    def get_oily_score(self):
        if self.oily == 'O':
            return 1
        elif self.oily == 'X':
            return -1
        else:
            return 0

    def get_dry_score(self):
        if self.dry == 'O':
            return 1
        elif self.dry == 'X':
            return -1
        else:
            return 0
    
    def get_sensitive_score(self):
        if self.sensitive == 'O':
            return 1
        elif self.sensitive == 'X':
            return -1
        else:
            return 0


# 상품 클래스
class Product(models.Model):
    imageId = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    gender = models.CharField(max_length=6)
    category = models.CharField(max_length=15)
    ingredientsList = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    monthlySales = models.IntegerField()

    def __str__(self):
        return self.name


# 피부 타입별 상품의 성분 점수 클래스
class ProductScore(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    oily_score = models.IntegerField()
    dry_score = models.IntegerField()
    sensitive_score = models.IntegerField()

    def __str__(self):
        return self.product.name
