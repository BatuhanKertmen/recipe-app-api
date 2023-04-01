from rest_framework import viewsets, permissions
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication

from core.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by("-id")
