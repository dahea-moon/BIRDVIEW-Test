from django.urls import reverse

from rest_framework.test import APITestCase

from myapp.item.models import Product, Ingredient


class ProductAPITest(APITestCase):
    
    fixtures = ['ingredients-data.json', 'products-data.json']

    def test_list_with_pagination(self):
        url = reverse('item:product_list')
        data = {
            'skin_type': 'oily',
            'page': 5,
        }
        response = self.client.get(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1000)
        self.assertEqual(len(response.data['results']), 50)
        self.assertEqual(response.data['results'][0]['id'], 923)

    
    def test_list_with_pagination_category(self):
        url = reverse('item:product_list')
        data = {
            'skin_type': 'sensitive',
            'page': 2,
            'category': 'basemakeup'
        }
        response = self.client.get(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 242)
        self.assertEqual(len(response.data['results']), 50)
        self.assertEqual(response.data['results'][48]['id'], 444)


    def test_list_with_iclude_ingredients(self):

        url = reverse('item:product_list')
        data = {
            'skin_type': 'dry',
            'page': 1,
            'include_ingredient': 'screw,multimedia'
            }
        response = self.client.get(url, data, content_type='application/json')

        count = 0
        if response.data['results']:
            for product in response.data['results']:
                ingredients = product['ingredients'].split(',')
                if 'screw' in ingredients and 'multimedia' in ingredients:
                    count += 1

        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, len(response.data['results']))
    

    def test_list_with_exclude_ingredients(self):

        url = reverse('item:product_list')
        data = {
            'skin_type': 'oily',
            'page': 1,
            'exclude_ingredient': 'unique,waiter'
        }
        response = self.client.get(url, data, content_type='application/json')
        
        count = 0
        if response.data['results']:
            for product in response.data['results']:
                ingredients = product['ingredients'].split(',')
                if 'unique' in ingredients or 'waiter' in ingredients:
                    count += 1
 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 0)
    

    def test_product_detail(self):
        url = reverse('item:product_detail', kwargs={'product_id': 10})
        data = {
            'skin_type': 'oily',
        }
        response = self.client.get(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 10)
        self.assertEqual(len(response.data['recommends']), 3)