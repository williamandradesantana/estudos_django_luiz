from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer

from tag.models import Tag

class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 2

class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    # def get(self, request):
    #     recipes = Recipe.objects.all()
    #     serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = RecipeSerializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(
    #         author_id=1, category_id=1,
    #         tags=[1,2]
    #     )
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class RecipeAPIv2Detail(APIView):
    def get_recipe(self, pk):
        recipe = get_object_or_404(
            Recipe.objects.all(), pk=pk
        )
        return recipe
    
    def get(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(instance=recipe, many=False, context={'request': request})
        return Response(serializer.data)
    
    def patch(self, request, pk):
        recipe = self.get_recipe(pk)
        
        serializer = RecipeSerializer(
            instance=recipe, 
            data=request.data, 
            many=False, 
            context={'request': request},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    def delete(self, request, pk):
        recipe = self.get_recipe(pk)
        recipe.delete()
        # recipe.is_published = False
        # recipe.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET"])
def tag_api_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    serializer = TagSerializer(instance=tag, many=False)
    return Response(serializer.data)