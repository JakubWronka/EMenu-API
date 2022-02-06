from rest_framework import viewsets

from .models import Recipe, Menu
from .serializers import RecipeSerializer, MenuSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()