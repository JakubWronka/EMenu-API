from django.test import TestCase

from menusapp.models import Menu, Recipe

from datetime import datetime, timedelta

from decimal import Decimal


class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        date_added = date_modified = datetime.now()
        Menu.objects.create(
            name='Test menu',
            description='Description of a test menu',
            added=date_added,
            modified=date_modified
        )
        Recipe.objects.create(
            name='Test recipe',
            description='Description of a test recipe',
            price=Decimal('17.99'),
            preparing_time=timedelta(minutes=15),
            is_vegetarian=True
        )

    def test_menu_expected_name(self):
        menu = Menu.objects.get(id=1)
        self.assertEqual('Test menu', menu.name)

    def test_menu_expected_description(self):
        menu = Menu.objects.get(id=1)
        self.assertEqual('Description of a test menu', menu.description)

    def test_recipe_expected_name(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual('Test recipe', recipe.name)

    def test_recipe_expected_description(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual('Description of a test recipe', recipe.description)
    
    def test_recipe_expected_price(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(Decimal('17.99'), recipe.price)

    def test_recipe_expected_preparing_time(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(timedelta(minutes=15), recipe.preparing_time)

    def test_recipe_expected_is_vegetarian(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(True, recipe.is_vegetarian)
