from django import forms
from recipes.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'recipe_name',
            'recipe_image',
            'ingredients',
            'steps'
        ]
