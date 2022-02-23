from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User


class APITestSetup(APITestCase):

    def setUp(self) -> None:
        self.user_data = {
            'username': 'jakub',
            'password': '1234',
            'email':'jakub@mail.com'
        }
        User.objects.create(
            username = self.user_data['username'],
            password = self.user_data['password'],
            email = self.user_data['email'],
        )
        self.user = User.objects.get(username=self.user_data['username'])
        self.test_menu_1_json_data = {
            "name": "Test menu 1", 
            "description": "Description for test menu 1", 
        }
        self.test_recipe_1_json_data = {
            "name": "Test recipe 1", 
            "description": "Description for test recipe 1", 
            "price": "13.90", 
            "preparing_time": "01:30:00", 
            "is_vegetarian": "false"
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

class TestAPIMethods(APITestSetup):

    def test_get_menus_unauth(self):
        result = self.client.get('/menus/')
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_get_menus_auth(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get('/menus/')
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_get_recipes_unauth(self):
        result = self.client.get('/recipes/')
        self.assertEqual(result.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_recipes_auth(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get('/recipes/')
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_post_menu_unauth(self):
        result = self.client.post('/menus/', self.test_menu_1_json_data, format='json')
        self.assertEqual(result.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_post_menu_auth(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.post('/menus/', self.test_menu_1_json_data, format='json')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_post_recipe_unauth(self):
        result = self.client.post('/recipes/', self.test_recipe_1_json_data, format='json')
        self.assertEqual(result.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_post_recipe_auth(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.post('/recipes/', self.test_recipe_1_json_data, format='json')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
