from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Recipe(models.Model):

    #fields for data
    recipe_name = models.CharField(max_length=20, help_text='Name of provided recipe')
    recipe_image = models.ImageField(upload_to = 'images/', default='static/recipes/default.png')
    ingredients = models.TextField()
    steps = models.TextField()
    recipe_url = models.SlugField(default='slug')

    def save(self, *args, **kwargs):
        self.recipe_url = slugify(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    #Will need views template for viewing all possible recipes when clicked
    def get_absolute_url(self):
        return reverse('model-detailed-view', args=[str(self.recipe_name)])

    def __str__(self):
        return self.recipe_name.replace(' ','_')
