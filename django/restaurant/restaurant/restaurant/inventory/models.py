from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField()
    menu_item = models.ForeignKey(
        "MenuItem", on_delete=models.CASCADE)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey("MenuItem", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    quantity = models.FloatField()


class Purchase(models.Model):
    menu_item = models.ForeignKey("MenuItem", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def purchase_item(self):
    #     if
