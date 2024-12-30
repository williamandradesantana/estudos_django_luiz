from django.test import TestCase
from django.contrib.auth.models import User

from recipes.models import Recipe, Category

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            email='username@email.com', 
            password='123456'
        )

        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            prepararion_time = 10,
            prepararion_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe preparation steps',
            preparation_steps_is_html = False,
            is_published=True,
        )

        return super().setUp()