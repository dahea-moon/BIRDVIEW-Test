from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

import random

from myapp.item.models import Product, Ingredient


class ProductListTest(TestCase):

    def test_list_with_pagination(self):
        url = reverse('item:product_list')
        data = {
            'skin_type': 'oily',
            'page': 5,
        }
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEqauls(response.count, 1000)
        self.assertEquals(len(response.results), 50)
        self.assertEquals(response.results[0].id, 923)

    
    def test_list_with_pagination_category(self):
        url = reverse('item:product_list')
        data = {
            'skin_type': 'sensitive',
            'page': 2,
            'category': 'basemakeup'
        }
        response = self.client.get(url, data, format='json')
        print('success')
        self.assertEquals(response.status_code, 200)
        self.assertEqauls(response.count, 242)
        self.assertEquals(len(response.results), 50)
        self.assertEquals(response.results[48].id, 444)


    # def list_with_iclude_ingredients(self):
        
    #     for i in range(1, 3):
    #         id = random.randint(1, 1001)
    #         f'ingredient{i}' = Ingredient.objects.get(id=id).name
    #     print(ingredient1)
    #     print(ingredient2)

    #     url = reverse('product_list')
    #     data = {
    #         'skin_type': 'dry',
    #         'page': 1,
    #         'include_ingredient': ingredient1,ingredient2
    #     }
    #     response = self.client.get(url, data, format='json')

    #     flag = False
    #     for product in response.result:
    #         ingredients = product.ingredients
    #         if ingredient1 in ingredients and ingredient2 in ingredients:
    #             flag = True

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(flag, True)
    
    # def list_with_exclude_ingredients(self):

    #     for i in range(1, 3):
    #         id = random.randint(1, 1001)
    #         f'ingredient{i}' = Ingredient.objects.get(id=id).name

    #     url = reverse('product_list')
    #     data = {
    #         'skin_type': 'oily',
    #         'page': 1,
    #         'exclude_ingredient': ingredient1,ingredient2
    #     }
    #     response = self.client.get(url, data, format='json')

    #     flag = True
    #     for product in response.result:
    #         ingredients = product.ingredients
    #         if ingredient1 in ingredients or ingredient2 in ingredients:
    #             flag = False

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(flag, True)
    
    
    

