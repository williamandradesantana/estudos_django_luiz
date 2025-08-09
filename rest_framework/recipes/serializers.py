from rest_framework import serializers

from django.contrib.auth.models import User

from tag.models import Tag

from .models import Recipe

class TagSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # slug = serializers.CharField()
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id", "title", "description", "author",
            "category", "tags", "public", "preparation",
            "tag_objects", "tag_links"
        ]

    public = serializers.BooleanField(source="is_published", read_only=True)
    preparation = serializers.SerializerMethodField(method_name="get_preparation")
    category = serializers.StringRelatedField(read_only=True)
    tag_objects = TagSerializer(source='tags', many=True, read_only=True)
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        view_name='recipes:recipes_api_v2_tag',
        read_only=True
    )

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'