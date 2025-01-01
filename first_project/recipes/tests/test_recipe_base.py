from django.test import TestCase
from django.contrib.auth.models import User

from recipes.models import Recipe, Category

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)
    
    def make_author(self,
        first_name='user',
        last_name='name',
        username='username',
        email='username@email.com', 
        password='123456'
        ):

        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
    
    def make_recipe(self, 
            category_data=None,
            author_data=None,
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
        ):

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title = title,
            description = description,
            slug = slug,
            prepararion_time = prepararion_time,
            prepararion_time_unit = prepararion_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published=is_published,
        )