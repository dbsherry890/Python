from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

admin.site.register([MenuItem, Purchase, RecipeRequirement, Ingredient])
