from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

from parameterized import parameterized

class CategoryModelTest(RecipeTestBase):
    def setUp(self):
        self.category = self.make_category(name='Category Testing')
        return super().setUp()
    
    def test_recipe_category_model_string_representation_is_name_field(self):
        self.assertEqual(str(self.category), self.category.name)
    

    @parameterized.expand([
        ('name', 65)
    ])

    def test_recipe_category_model_name_max_length_is_65_chars(self, field, max_length):
        setattr(self.category, field, 'a' * (max_length + 0))

        with self.assertRaises(ValidationError):
            self.category.full_clean()