from django.db import models

# Create your models here.
class Recipes(models.Model):

    #fields for data
    recipe_name = models.CharField(max_length=20, help_text='Name of provided recipe')
    #recipe_image = models.ImageField()
    #Queryset was acting strange with images for some reason
    ingredients = models.TextField()
    steps = models.TextField()

    def __str__(self):
        return self.recipe_name
