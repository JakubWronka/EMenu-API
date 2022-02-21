from django.db.models import Count

from rest_framework import viewsets, permissions

from .models import Recipe, Menu
from .serializers import RecipeSerializer, MenuSerializer
from .filters import MenuFilter

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    ordering_fields = []

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = MenuFilter
    ordering_fields = ['name', 'recipes_count']

    def get_queryset(self):
        return Menu.objects.annotate(recipes_count=Count('recipes')).all()
