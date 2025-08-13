from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer

from tag.models import Tag

@api_view(["get", "post"])
def recipe_api_list(request):
    
    if request.method == "GET":
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = RecipeSerializer(data=request.data, context={'request': request})
        
        serializer.is_valid(raise_exception=True)
        serializer.save(
            author_id=1, category_id=1,
            tags=[1,2]
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PATCH", "DELETE"])
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.all(), pk=pk
    )

    if request.method == "GET":
        serializer = RecipeSerializer(instance=recipe, many=False, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = RecipeSerializer(
            instance=recipe, 
            data=request.data, 
            many=False, 
            context={'request': request},
            partial=True)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET"])
def tag_api_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    serializer = TagSerializer(instance=tag, many=False)
    return Response(serializer.data)