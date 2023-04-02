from rest_framework import viewsets, permissions
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.RecipeSerializer
        return serializers.RecipeDetailSerializer
