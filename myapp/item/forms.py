from django import forms
from .models import Product, Ingredient


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('imageId', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales')


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'oily', 'dry', 'sensitive')