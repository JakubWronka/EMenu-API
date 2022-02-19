from rest_framework import serializers
from .models import Recipe, Menu

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'price', 'preparing_time', 'added', 'modified', 'is_vegetarian']

class MenuSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = ['id', 'name', 'added', 'modified', 'recipes']
