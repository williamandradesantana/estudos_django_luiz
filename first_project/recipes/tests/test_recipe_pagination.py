from django.urls import reverse
from django.http.request import HttpRequest
from .test_recipe_base import RecipeTestBase
from utils.pagination import make_pagination
class RecipePaginationTest(RecipeTestBase):

    def test_verify_if_pagination_is_working_in_home(self):
        # Need a recipe for this test
        recipes = [
            self.make_recipe(slug=str(i), title=f'Recipe {i}', author_data={'username': str(i)}) for i in range(10)
        ]

        url = reverse('recipes:home')
        request = HttpRequest()
        request.GET = {'page': '1'}

        response = self.client.get(url)
        page_obj, pagination_range = make_pagination(request, recipes, 9, 2)

        self.assertIn('Recipe 1', response.content.decode('utf-8'))
        self.assertEqual(len(page_obj.object_list), 9)
        self.assertEqual(response.status_code, 200)
    
    def test_pagination_in_another_pages(self):
        # Need a recipe for this test
        recipes = [
            self.make_recipe(slug=str(i), title=f'Recipe {i}', author_data={'username': str(i)}) for i in range(20)
        ]
        url = reverse('recipes:home')
        request = HttpRequest()
        request.GET = {'page': '2'}

        response = self.client.get(url)
        page_obj, pagination_range = make_pagination(request, recipes, 9, 2)

        self.assertIn('Recipe 1', response.content.decode('utf-8'))
        self.assertEqual(len(page_obj.object_list), 9)
        self.assertEqual(response.status_code, 200)