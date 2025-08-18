from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer

from tag.models import Tag

class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 2

class RecipeAPIv2ViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["example"] = "This is in context now"
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get('category_id', '')
        
        if category_id != ''  and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)
        return qs

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        recipe = self.get_queryset().filter(pk=pk).first()
        serializer = RecipeSerializer(
            instance=recipe,
            many=False,
            data=request.data,
            context={'request': request},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def tag_api_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    serializer = TagSerializer(instance=tag, many=False)
    return Response(serializer.data)