from django.contrib import admin
from . import models

# Register your models here.
# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
admin.site.register(models.Product)
admin.site.register(models.Ingredient)
admin.site.register(models.ProductScore)