from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparing_time = models.DurationField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_vegetarian = models.BooleanField()

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    recipes = models.ManyToManyField(Recipe, related_name='menus', blank=True)
