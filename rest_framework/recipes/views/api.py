from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer

from tag.models import Tag

@api_view(["GET"])
def recipe_api_list(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(["GET"])
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.all(), pk=pk
    )
    serializer = RecipeSerializer(instance=recipe, many=False, context={'request': request})
    return Response(serializer.data)
    
    # recipe = Recipe.objects.all().filter(pk=pk).first()
    # if recipe:
    #     serializer = RecipeSerializer(instance=recipe, many=False)
    #     return Response(serializer.data)
    # else:
    #     return Response({'detail': 'eita'}, status=status.HTTP_418_IM_A_TEAPOT)

@api_view(["GET"])
def tag_api_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    serializer = TagSerializer(instance=tag, many=False)
    return Response(serializer.data)