from django.db import models
from django.urls import reverse

class Recipe(models.Model):

    #fields for data
    recipe_name = models.CharField(max_length=20, help_text='Name of provided recipe')
    recipe_image = models.ImageField(upload_to = 'images/', default='static/recipes/default.png')
    ingredients = models.TextField()
    steps = models.TextField()

    #Will need views template for viewing all possible recipes when clicked
    def get_absolute_url(self):
        return reverse('model-detailed-view', args=[str(self.recipe_name)])

    def __str__(self):
        return self.recipe_name.replace(' ','_')
